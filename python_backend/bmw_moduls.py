import os

os.environ['PATH'] = r"C:\EDIABAS\bin;" + os.environ.get('PATH', '')

if hasattr(os, 'add_dll_directory'):
    try:
        os.add_dll_directory(r"C:\EDIABAS\bin")
    except Exception:
        pass

import time
from pydiabas import PyDIABAS

class BMWLightModule:
    def __init__(self, ecu, bmw_connection):
        self._ecu = ecu
        self.bmw = bmw_connection

    def connect(self):
        print("Connecting to", self._ecu)

    def turn_off(self, lights): pass

    def turn_on(self, lights): pass

    def farewell(self): pass

    def lights_show_run(self, cycle, off_time, on_time):
        for i in range(cycle):
            for lights in self.lights_show:

                self.turn_on(lights)
                time.sleep(on_time)
                self.turn_off(lights)

                if off_time > 0:
                    time.sleep(off_time)

        time.sleep(0.3)
        self.farevell()
        time.sleep(1)

class lszModule(BMWLightModule):           #E46, E83, E85
    def __init__(self, bmw_connection):
        super().__init__(ecu = "LSZ", bmw_connection = bmw_connection)
        self.lights_show = ["SL_LV", "SL_RV", "BLK_LV", "REL_NSW", "FL_L", "FL_R", "BLK_RV"]
        self.music_show = [
            ["FL_L", "FL_R"],
            ["BLK_LV", "BLK_RV"],
            ["FL_L", "FL_R", "REL_NSW"],
            ["BLK_LV", "BLK_RV", "REL_NSW"]]

    def turn_on(self, lights):
        self.bmw.job(self._ecu, "STEUERN_IO", lights)
        print(f"{self._ecu}: STEUERN_IO: {lights} [*]")

    def turn_off(self, lights):
        self.bmw.job(self._ecu, "DIAGNOSE_ENDE")
        print(f"{self._ecu}: DIAGNOSE_ENDE: {lights} [-]")

    def farewell(self):
        self.bmw.job(self._ecu, "STEUERN_IO", self.lights_show)


    class lcmModule(BMWLightModule):            # E38, E39, E53
        def __init__(self, bmw_connection):
            super().__init__(ecu = "LCM_III", bmw_connection = bmw_connection)
            self.lihts_show = []
            self.music_show = []

        def turn_on(self, lights):
            self.bmw.job(self._ecu, "STATUS_VORGEBEN", lights)
            print(f"{self._ecu}: STATUS_VORGEBEN: {lights} [*]")

        def turn_off(self, lights):
            self.bmw.job(self._ecu, "DIAGNOSE_ENDE", lights)
            print(f"{self._ecu}: DIAGNOSE_ENDE: {lights} [-]")

        def farewell(self):
            self.bmw.job(self._ecu, "STATUS_VORGEBEN", self.lihts_show)


    class frm_70Module(BMWLightModule):            # E70, E71, E72
        def __init__(self, bmw_connection):
            super().__init__(ecu = "FRM_70", bmw_connection = bmw_connection)
            self.lights_show = []
            self.music_show = []

        def turn_on(self, lights):
            self.bmw.job(self._ecu, "STEUERN_LAMPEN_PWM", f"{lights};100")
            print(f"{self._ecu}: STEUERN_LAMPEN_PWM: {lights} [*]")

        def turn_off(self, lights):
            self.bmw.job(self._ecu, "STEUERN_LAMPEN_PWM", f"{lights};0")
            print(f"{self._ecu}: STEUERN_LAMPEN_PWM: {lights} [*]")

        def farewell(self):
            for light in self.lights_show:
                self.bmw.job(self._ecu, "STEUERN_LAMPEN_PWM", f"{light};100")
                time.sleep(0.15)

            time.sleep(1.0)

            for pwm in range(100, -1, -10):
                for light in self.lights_show:
                    self.bmw.job(self._ecu, "STEUERN_LAMPEN_PWM", f"{light};{pwm}")
                time.sleep(0.04)


    class frm_87Module(BMWLightModule):             # E81, E82, E87, E88, E90-93
        def __init__(self, bmw_connection):
            super().__init__(ecu="FRM_87", bmw_connection=bmw_connection)
            self.lights_show = []
            self.music_show = []

        def turn_on(self, lights):
            self.bmw.job(self._ecu, "STEUERN_LAMPEN_PWM", f"{lights};100")
            print(f"{self._ecu}: STEUERN_LAMPEN_PWM: {lights} [*]")

        def turn_off(self, lights):
            self.bmw.job(self._ecu, "STEUERN_LAMPEN_PWM", f"{lights};0")
            print(f"{self._ecu}: STEUERN_LAMPEN_PWM: {lights} [*]")

        def farewell(self):
            for light in self.lights_show:
                self.bmw.job(self._ecu, "STEUERN_LAMPEN_PWM", f"{light};100")
                time.sleep(0.15)

            time.sleep(1.0)

            for pwm in range(100, -1, -10):
                for light in self.lights_show:
                    self.bmw.job(self._ecu, "STEUERN_LAMPEN_PWM", f"{light};{pwm}")
                time.sleep(0.04)

