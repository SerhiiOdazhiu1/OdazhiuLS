Imports System.ComponentModel
Imports System.Diagnostics
Imports System.IO

Public Class Form1
    Private timeLeft As Integer
    Private vybraneShow As String = ""
    Private pythonProcess As Process
    Private musicSettingForm As Form

    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles Me.Load
        cmbChassis.Items.Add("E38")
        cmbChassis.Items.Add("E39")
        cmbChassis.Items.Add("E46")
        cmbChassis.Items.Add("E53")
        cmbChassis.Items.Add("E60-E61")
        cmbChassis.Items.Add("E63-E64")
        cmbChassis.Items.Add("E65-E66")
        cmbChassis.Items.Add("E70-E71-E72")
        cmbChassis.Items.Add("E81-E82-E87-E88")
        cmbChassis.Items.Add("E83")
        cmbChassis.Items.Add("E84")
        cmbChassis.Items.Add("E85-E86")
        cmbChassis.Items.Add("E89")
        cmbChassis.Items.Add("E90-E91-E92-E93")

        picCar.SizeMode = PictureBoxSizeMode.StretchImage
        picCar.Image = Image.FromFile(Application.StartupPath & "\images\BMW.jpg")

        btnCustom.Enabled = False
        btnMusic.Enabled = False
        btnDefault.Enabled = False
        btnStop.Enabled = False
    End Sub

    Private Sub cmbChassis_SelectedIndexChanged(sender As Object, e As EventArgs) Handles cmbChassis.SelectedIndexChanged
        btnCustom.Enabled = True
        btnDefault.Enabled = True
        btnMusic.Enabled = True

        Dim chassisName As String = cmbChassis.SelectedItem.ToString

        Dim pathJPG As String = Application.StartupPath & "\images\" & chassisName & ".jpg"
        Dim pathPNG As String = Application.StartupPath & "\images\" & chassisName & ".png"
        Dim pathJFIF As String = Application.StartupPath & "\images\" & chassisName & ".jfif"

        If System.IO.File.Exists(pathJPG) Then
            picCar.Image = Image.FromFile(pathJPG)
        ElseIf System.IO.File.Exists(pathPNG) Then
            picCar.Image = Image.FromFile(pathPNG)
        ElseIf System.IO.File.Exists(pathJFIF) Then
            picCar.Image = Image.FromFile(pathJFIF)
        Else
            picCar.Image = Nothing
        End If
    End Sub

    Private Sub tmrStartTime_Tick(sender As Object, e As EventArgs) Handles tmrStartTime.Tick
        If timeLeft > 0 Then
            timeLeft -= 1
            txtTime.Text = timeLeft.ToString()
        Else
            tmrStartTime.Stop()
            'txtTime.Text = "Start!"

            Select Case vybraneShow
                Case "Default"
                    Dim timeOn As String = "0.1"
                    Dim timeOff As String = "0.03"
                    Dim cycle As String = "8"
                    Dim argumentLamps As String = "FL_L,FL_R,REL_NSW,BLK_LV,SL_LV,FL_L,FL_R,SL_RV,BLK_RV"
                    Dim allArguments As String = $"{timeOn} {timeOff} {cycle} {argumentLamps}"

                    RunPythonScript("light_show.py", allArguments)

                Case "Music"
                    OpenMusicSettingsForm()
                    RunPythonScript("music_show.py", "")

                Case "Custom"
                    Dim timeOn As String = Form2.finalTimeIg
                    Dim timeOff As String = Form2.finalTimeBet
                    Dim cycle As String = Form2.finalCycle
                    Dim argumentLamps As String = String.Join(",", Form2.finalLamps)
                    Dim allArguments As String = $"{timeOn} {timeOff} {cycle} {argumentLamps}"

                    RunPythonScript("light_show.py", allArguments)
            End Select
        End If
    End Sub

    Private Sub RunPythonScript(scriptName As String, arguments As String)
        Try
            Dim pInfo As New ProcessStartInfo
            pInfo.FileName = Path.Combine(Application.StartupPath, ".venv\Scripts\python.exe")
            pInfo.Arguments = $"{scriptName} {arguments}"
            pInfo.WorkingDirectory = Application.StartupPath

            pInfo.UseShellExecute = False
            pInfo.CreateNoWindow = True 'Поменять после симуляции.

            pythonProcess = New Process()
            pythonProcess.StartInfo = pInfo

            pythonProcess.EnableRaisingEvents = True
            AddHandler pythonProcess.Exited, AddressOf PythonProcess_Exited

            pythonProcess.Start()
        Catch ex As Exception
            MsgBox("Error start: " & ex.Message, MsgBoxStyle.Critical, "Error")
        End Try
    End Sub

    Private Sub ResetInterface()
        txtTime.ReadOnly = False
        txtTime.Text = ""

        btnCustom.Enabled = True
        btnDefault.Enabled = True
        btnMusic.Enabled = True
        btnStop.Enabled = False
    End Sub

    Private Sub PythonProcess_Exited(sender As Object, e As EventArgs)
        Me.Invoke(Sub()
                      If musicSettingForm IsNot Nothing AndAlso Not musicSettingForm.IsDisposed Then
                          musicSettingForm.Close()
                      End If
                      ResetInterface()
                  End Sub)
    End Sub

    'Кнопка кастомного шоу
    Private Sub btnCustom_Click(sender As Object, e As EventArgs) Handles btnCustom.Click
        If Not ChecTime() Then Return

        If Form2.ShowDialog() = DialogResult.OK Then
            StartCountdown("Custom")
        End If
    End Sub

    'Кнопка дефолта
    Private Sub btnDefault_Click(sender As Object, e As EventArgs) Handles btnDefault.Click
        If Not ChecTime() Then Return

        StartCountdown("Default")
    End Sub

    'Кнопка музык. шоу
    Private Sub btnMusic_Click(sender As Object, e As EventArgs) Handles btnMusic.Click
        If Not ChecTime() Then Return

        StartCountdown("Music")
    End Sub

    Private Sub StartCountdown(showType As String)
        vybraneShow = showType

        btnStop.Enabled = True
        btnCustom.Enabled = False
        btnDefault.Enabled = False
        btnMusic.Enabled = False

        txtTime.ReadOnly = True

        timeLeft = CInt(txtTime.Text)
        tmrStartTime.Start()
    End Sub

    Private Sub OpenMusicSettingsForm()
        If musicSettingForm IsNot Nothing AndAlso Not musicSettingForm.IsDisposed Then
            musicSettingForm.Close()
        End If

        musicSettingForm = New Form()
        musicSettingForm.Text = "Setting bass"
        musicSettingForm.Size = New Size(350, 150)
        musicSettingForm.StartPosition = FormStartPosition.CenterScreen
        musicSettingForm.FormBorderStyle = FormBorderStyle.FixedToolWindow
        musicSettingForm.TopMost = True

        Dim lblValue As New Label()
        lblValue.Text = "Threshold: 25"
        lblValue.Font = New Font("Segoe UI", 10, FontStyle.Bold)
        lblValue.AutoSize = True
        lblValue.Location = New Point(12, 9)

        Dim trkThreshold As New TrackBar()
        trkThreshold.Minimum = 10
        trkThreshold.Maximum = 80
        trkThreshold.Value = 25
        trkThreshold.TickFrequency = 5
        trkThreshold.Size = New Size(300, 45)
        trkThreshold.Location = New Point(12, 32)

        File.WriteAllText(Application.StartupPath & "\threshold.txt", "25")

        AddHandler trkThreshold.ValueChanged, Sub(sender As Object, e As EventArgs)
                                                  lblValue.Text = "Threshold: " & trkThreshold.Value.ToString()
                                                  Try
                                                      File.WriteAllText(Application.StartupPath & "\threshold.txt", trkThreshold.Value.ToString())
                                                  Catch ex As Exception
                                                  End Try
                                              End Sub

        musicSettingForm.Controls.Add(lblValue)
        musicSettingForm.Controls.Add(trkThreshold)
        musicSettingForm.Show()
    End Sub

    'Stop
    Private Sub btnStop_Click(sender As Object, e As EventArgs) Handles btnStop.Click
        tmrStartTime.Stop()

        If pythonProcess IsNot Nothing AndAlso Not pythonProcess.HasExited Then
            RemoveHandler pythonProcess.Exited, AddressOf PythonProcess_Exited
            pythonProcess.Kill()
        End If

        If musicSettingForm IsNot Nothing AndAlso Not musicSettingForm.IsDisposed Then
            musicSettingForm.Close()
        End If

        Try
            Dim forceStopLight As New ProcessStartInfo(Path.Combine(Application.StartupPath, ".venv\Scripts\python.exe"), "light_show.py stop")
            forceStopLight.CreateNoWindow = True
            forceStopLight.UseShellExecute = False
            Process.Start(forceStopLight)
        Catch ex As Exception
        End Try

        Try
            Dim forceStopMusic As New ProcessStartInfo(Path.Combine(Application.StartupPath, ".venv\Scripts\python.exe"), "music_show.py stop")
            forceStopMusic.CreateNoWindow = True
            forceStopMusic.UseShellExecute = False
            Process.Start(forceStopMusic)
        Catch ex As Exception
        End Try

        ResetInterface()
    End Sub

    Private Sub txtTime_KeyPress(sender As Object, e As KeyPressEventArgs) Handles txtTime.KeyPress
        If Not Char.IsDigit(e.KeyChar) AndAlso e.KeyChar <> ChrW(Keys.Back) Then
            e.Handled = True
        End If

        If txtTime.Text.Length = 0 AndAlso e.KeyChar = "0"c Then
            e.Handled = True
        End If
    End Sub

    Private Function ChecTime() As Boolean
        If txtTime.Text.Trim = "" Then
            MsgBox("Please enter the correct time before starting!" & vbCrLf & "Введите коректное время перед пуском!", MsgBoxStyle.Critical, "Error input")
            Return False
        End If

        Return True
    End Function

End Class
