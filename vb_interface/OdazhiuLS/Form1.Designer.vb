<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()>
Partial Class Form1
    Inherits System.Windows.Forms.Form

    'Form overrides dispose to clean up the component list.
    <System.Diagnostics.DebuggerNonUserCode()>
    Protected Overrides Sub Dispose(disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.
    'Do not modify it using the code editor.
    <System.Diagnostics.DebuggerStepThrough()>
    Private Sub InitializeComponent()
        components = New ComponentModel.Container()
        Dim resources As System.ComponentModel.ComponentResourceManager = New System.ComponentModel.ComponentResourceManager(GetType(Form1))
        btnDefault = New Button()
        btnStop = New Button()
        btnMusic = New Button()
        btnCustom = New Button()
        lblTime = New Label()
        txtTime = New TextBox()
        tmrStartTime = New Timer(components)
        lblSecond = New Label()
        grpSetting = New GroupBox()
        lblChassis = New Label()
        cmbChassis = New ComboBox()
        picCar = New PictureBox()
        grpSetting.SuspendLayout()
        CType(picCar, ComponentModel.ISupportInitialize).BeginInit()
        SuspendLayout()
        ' 
        ' btnDefault
        ' 
        btnDefault.Font = New Font("Segoe UI", 13.8F, FontStyle.Bold, GraphicsUnit.Point, CByte(204))
        btnDefault.Location = New Point(144, 141)
        btnDefault.Name = "btnDefault"
        btnDefault.Size = New Size(126, 95)
        btnDefault.TabIndex = 0
        btnDefault.Text = "Default Show"
        btnDefault.UseVisualStyleBackColor = True
        ' 
        ' btnStop
        ' 
        btnStop.Font = New Font("Segoe UI Black", 16.2F, FontStyle.Bold, GraphicsUnit.Point, CByte(204))
        btnStop.Location = New Point(12, 242)
        btnStop.Name = "btnStop"
        btnStop.Size = New Size(390, 80)
        btnStop.TabIndex = 7
        btnStop.Text = "STOP"
        btnStop.UseVisualStyleBackColor = True
        ' 
        ' btnMusic
        ' 
        btnMusic.Font = New Font("Segoe UI", 13.8F, FontStyle.Bold, GraphicsUnit.Point, CByte(204))
        btnMusic.Location = New Point(12, 141)
        btnMusic.Name = "btnMusic"
        btnMusic.Size = New Size(126, 95)
        btnMusic.TabIndex = 8
        btnMusic.Text = "Music Show"
        btnMusic.UseVisualStyleBackColor = True
        ' 
        ' btnCustom
        ' 
        btnCustom.Font = New Font("Segoe UI", 13.8F, FontStyle.Bold, GraphicsUnit.Point, CByte(204))
        btnCustom.Location = New Point(276, 141)
        btnCustom.Name = "btnCustom"
        btnCustom.Size = New Size(126, 95)
        btnCustom.TabIndex = 9
        btnCustom.Text = "Custom Show"
        btnCustom.UseVisualStyleBackColor = True
        ' 
        ' lblTime
        ' 
        lblTime.AutoSize = True
        lblTime.Font = New Font("Segoe UI", 9F, FontStyle.Regular, GraphicsUnit.Point, CByte(204))
        lblTime.Location = New Point(6, 78)
        lblTime.Name = "lblTime"
        lblTime.Size = New Size(96, 20)
        lblTime.TabIndex = 10
        lblTime.Text = "Time to start:"
        ' 
        ' txtTime
        ' 
        txtTime.Location = New Point(121, 75)
        txtTime.Name = "txtTime"
        txtTime.Size = New Size(33, 27)
        txtTime.TabIndex = 11
        ' 
        ' tmrStartTime
        ' 
        tmrStartTime.Interval = 1000
        ' 
        ' lblSecond
        ' 
        lblSecond.AutoSize = True
        lblSecond.Location = New Point(160, 78)
        lblSecond.Name = "lblSecond"
        lblSecond.Size = New Size(59, 20)
        lblSecond.TabIndex = 12
        lblSecond.Text = "second."
        ' 
        ' grpSetting
        ' 
        grpSetting.Controls.Add(lblChassis)
        grpSetting.Controls.Add(cmbChassis)
        grpSetting.Controls.Add(txtTime)
        grpSetting.Controls.Add(lblTime)
        grpSetting.Controls.Add(lblSecond)
        grpSetting.Location = New Point(12, 12)
        grpSetting.Name = "grpSetting"
        grpSetting.Size = New Size(225, 123)
        grpSetting.TabIndex = 13
        grpSetting.TabStop = False
        grpSetting.Text = "Setting"
        ' 
        ' lblChassis
        ' 
        lblChassis.AutoSize = True
        lblChassis.Location = New Point(6, 37)
        lblChassis.Name = "lblChassis"
        lblChassis.Size = New Size(56, 20)
        lblChassis.TabIndex = 14
        lblChassis.Text = "Chassis"
        ' 
        ' cmbChassis
        ' 
        cmbChassis.DropDownStyle = ComboBoxStyle.DropDownList
        cmbChassis.FormattingEnabled = True
        cmbChassis.Location = New Point(93, 34)
        cmbChassis.Name = "cmbChassis"
        cmbChassis.Size = New Size(126, 28)
        cmbChassis.TabIndex = 13
        ' 
        ' picCar
        ' 
        picCar.Location = New Point(243, 23)
        picCar.Name = "picCar"
        picCar.Size = New Size(159, 111)
        picCar.TabIndex = 14
        picCar.TabStop = False
        ' 
        ' Form1
        ' 
        AutoScaleDimensions = New SizeF(8F, 20F)
        AutoScaleMode = AutoScaleMode.Font
        ClientSize = New Size(414, 332)
        Controls.Add(picCar)
        Controls.Add(grpSetting)
        Controls.Add(btnCustom)
        Controls.Add(btnMusic)
        Controls.Add(btnStop)
        Controls.Add(btnDefault)
        FormBorderStyle = FormBorderStyle.FixedSingle
        Icon = CType(resources.GetObject("$this.Icon"), Icon)
        MaximizeBox = False
        Name = "Form1"
        Text = "OdazhiuLS"
        grpSetting.ResumeLayout(False)
        grpSetting.PerformLayout()
        CType(picCar, ComponentModel.ISupportInitialize).EndInit()
        ResumeLayout(False)
    End Sub

    Friend WithEvents btnDefault As Button
    Friend WithEvents lblSecond As Label
    Friend WithEvents TextBox1 As TextBox
    Friend WithEvents PictureBox1 As PictureBox
    Friend WithEvents Button2 As Button
    Friend WithEvents Button3 As Button
    Friend WithEvents btnStop As Button
    Friend WithEvents btnMusic As Button
    Friend WithEvents btnCustom As Button
    Friend WithEvents lblTime As Label
    Friend WithEvents txtTime As TextBox
    Friend WithEvents tmrStartTime As Timer
    Friend WithEvents grpSetting As GroupBox
    Friend WithEvents lblChassis As Label
    Friend WithEvents cmbChassis As ComboBox
    Friend WithEvents picCar As PictureBox

End Class
