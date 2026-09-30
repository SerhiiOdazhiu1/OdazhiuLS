import os
import random

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
        self.flash_time = 0.015
        self.cooldown = 0.03

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
        self.farewell()
        time.sleep(1)

    def music_turn_on(self, lights_arr):
        for lights in lights_arr:
            self.bmw.job(self._ecu, "STEUERN_LAMPEN_PWM", f"{lights};100")

    def music_turn_off(self, lights_arr):
        for lights in lights_arr:
            self.bmw.job(self._ecu, "STEUERN_LAMPEN_PWM", f"{lights};0")

    def music_beat(self):
        light_random = random.choice(self.music_show)

        self.music_turn_on(light_random)
        time.sleep(self.flash_time)
        self.music_turn_off(light_random)

    def stop(self):
        try:
            self.bmw.job(self._ecu, "DIAGNOSE_ENDE")
            print(f"{self._ecu} - stop")
        except:
            pass

class lszModule(BMWLightModule):           #E46, E83, E85
    def __init__(self, bmw_connection):
        super().__init__(ecu = "LSZ", bmw_connection = bmw_connection)
        self.lights_show = ["SL_LV", "SL_RV", "BLK_LV", "REL_NSW", "FL_L", "FL_R", "BLK_RV"]
        self.music_show = [
            ["FL_L", "FL_R"],
            ["BLK_LV", "BLK_RV"],
            ["FL_L", "FL_R", "REL_NSW"],
            ["BLK_LV", "BLK_RV", "REL_NSW"]]
        self.flash_time = 0.03
        self.cooldown = 0.06

    def turn_on(self, lights):
        self.bmw.job(self._ecu, "STEUERN_IO", lights)
        print(f"{self._ecu}: STEUERN_IO: {lights} [*]")

    def turn_off(self, lights):
        self.bmw.job(self._ecu, "DIAGNOSE_ENDE")
        print(f"{self._ecu}: DIAGNOSE_ENDE: {lights} [-]")

    def farewell(self):
        self.bmw.job(self._ecu, "STEUERN_IO", self.lights_show)

    def music_beat(self):
        light_random = random.choice(self.music_show)

        self.bmw.job(self._ecu, "STEUERN_IO", light_random)
        time.sleep(self.flash_time)
        self.bmw.job(self._ecu, "DIAGNOSE_ENDE")


class lcmModule(BMWLightModule):            # E38, E39, E53
    def __init__(self, bmw_connection):
        super().__init__(ecu = "LCM_III", bmw_connection = bmw_connection)
        self.lights_show = ["BLK_LV", "SL_LV", "SL_RV", "BLK_RV", "NSW_R", "NSW_L"]
        self.music_show = [
            ["BLK_LV", "BLK_RV", "NSW_R", "NSW_L"],
            ["AL_L", "AL_R", "NSW_R", "NSW_L"],
            ["BLK_LV", "BLK_RV"],
            ["AL_L", "AL_R"]]
        self.flash_time = 0.03
        self.cooldown = 0.06

    def turn_on(self, lights):
        self.bmw.job(self._ecu, "STATUS_VORGEBEN", lights)
        print(f"{self._ecu}: STATUS_VORGEBEN: {lights} [*]")

    def turn_off(self, lights):
        self.bmw.job(self._ecu, "DIAGNOSE_ENDE", lights)
        print(f"{self._ecu}: DIAGNOSE_ENDE: {lights} [-]")

    def farewell(self):
        self.bmw.job(self._ecu, "STATUS_VORGEBEN", self.lights_show)

    def music_beat(self):
        light_random = random.choice(self.music_show)

        self.bmw.job(self._ecu, "STATUS_VORGEBEN", light_random)
        time.sleep(self.flash_time)
        self.bmw.job(self._ecu, "DIAGNOSE_ENDE")


class frm_70Module(BMWLightModule):            # E70, E71, E72
    def __init__(self, bmw_connection):
        super().__init__(ecu = "FRM_70", bmw_connection = bmw_connection)
        self.lights_show = [
            "AUSGANG_FRA_RECHTS_VORN",  # П поворотник
            "AUSGANG_DRL_RECHTS",  # П глазки
            "AUSGANG_DRL_LINKS",  # Л глазки
            "AUSGANG_FRA_LINKS_VORN",  # Л поворотник
            "AUSGANG_NSW_LINKS",  # Л туманка
            "AUSGANG_NSW_RECHTS"]  # П туманка
        self.music_show = [
            ["AUSGANG_FRA_RECHTS_VORN", "AUSGANG_FRA_LINKS_VORN", "AUSGANG_NSW_LINKS", "AUSGANG_NSW_RECHTS"],
            ["AUSGANG_DRL_RECHTS", "AUSGANG_DRL_LINKS", "AUSGANG_NSW_LINKS", "AUSGANG_NSW_RECHTS"],
            ["AUSGANG_FRA_RECHTS_VORN", "AUSGANG_FRA_LINKS_VORN"],
            ["AUSGANG_DRL_RECHTS", "AUSGANG_DRL_LINKS"]
        ]

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
        self.lights_show = [
            "AUSGANG_FRA_RECHTS_VORN",
            "AUSGANG_BEGRL_RECHTS",
            "AUSGANG_SL_BL_RECHTS_1",
            "AUSGANG_BEGRL_LINKS",
            "AUSGANG_SL_BL_LINKS_1",                #Сразу и дхо и габариты что проглотит то и загорит
            "AUSGANG_FRA_LINKS_VORN",
            "AUSGANG_NSW_LINKS",
            "AUSGANG_NSW_RECHTS"
        ]
        self.music_show = [
            ["AUSGANG_FRA_RECHTS_VORN", "AUSGANG_FRA_LINKS_VORN", "AUSGANG_NSW_LINKS", "AUSGANG_NSW_RECHTS"],
            ["AUSGANG_FL_LINKS", "AUSGANG_FL_RECHTS", "AUSGANG_NSW_LINKS", "AUSGANG_NSW_RECHTS"], #Вместо глащок дальний
            ["AUSGANG_FRA_RECHTS_VORN", "AUSGANG_FRA_LINKS_VORN"],
            ["AUSGANG_FL_LINKS", "AUSGANG_FL_RECHTS"]
        ]

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

class lm_60Module(BMWLightModule):             # E60, E61, E63, E64
    def __init__(self, bmw_connection):
        super().__init__(ecu="LM_60", bmw_connection=bmw_connection)
        self.lights_show = [
            "AUSGANG_FRA_RECHTS_VORN_1",
            "AUSGANG_BEGRL_RECHTS",
            "AUSGANG_BEGRL_LINKS",
            "AUSGANG_FRA_LINKS_VORN_1",
            "AUSGANG_NSW_LINKS",
            "AUSGANG_NSW_RECHTS",
        ]
        self.music_show = [
            ["AUSGANG_FL_LINKS", "AUSGANG_FL_RECHTS", "AUSGANG_NSW_LINKS", "AUSGANG_NSW_RECHTS"],
            ["AUSGANG_FRA_RECHTS_VORN_1", "AUSGANG_FRA_LINKS_VORN_1", "AUSGANG_NSW_LINKS", "AUSGANG_NSW_RECHTS"],
            ["AUSGANG_FL_LINKS", "AUSGANG_FL_RECHTS"],
            ["AUSGANG_FRA_RECHTS_VORN_1", "AUSGANG_FRA_LINKS_VORN_1"]
        ]

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

class lm_65Module(BMWLightModule):             # E65, E66
    def __init__(self, bmw_connection):
        super().__init__(ecu="LM_65", bmw_connection=bmw_connection)
        self.lights_show = [
            "AUSGANG_FRA_RECHTS_VORN_1",
            "AUSGANG_BEGRL_RECHTS",
            "AUSGANG_BEGRL_LINKS",
            "AUSGANG_FRA_LINKS_VORN_1",
            "AUSGANG_NSW_LINKS",
            "AUSGANG_NSW_RECHTS",
        ]
        self.music_show = [
            ["AUSGANG_FL_LINKS", "AUSGANG_FL_RECHTS", "AUSGANG_NSW_LINKS", "AUSGANG_NSW_RECHTS"],
            ["AUSGANG_FRA_RECHTS_VORN_1", "AUSGANG_FRA_LINKS_VORN_1", "AUSGANG_NSW_LINKS", "AUSGANG_NSW_RECHTS"],
            ["AUSGANG_FL_LINKS", "AUSGANG_FL_RECHTS"],
            ["AUSGANG_FRA_RECHTS_VORN_1", "AUSGANG_FRA_LINKS_VORN_1"]
        ]

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


def get_module_for_chassis(chassis, bmw_connection):
    mapping = {
        "E38": lcmModule,
        "E39": lcmModule,
        "E46": lszModule,
        "E53": lcmModule,
        "E60-E61": lm_60Module,
        "E63-E64": lm_60Module,
        "E65-E66": lm_65Module,
        "E70-E71-E72": frm_70Module,
        "E81-E82-E87-E88": frm_87Module,
        "E83": lszModule,
        "E90-E91-E92-E93": frm_87Module,
    }

    module_class = mapping.get(chassis)
    if module_class:
        return module_class(bmw_connection)
    else:
        raise ValueError(f"{chassis} is not a valid chassis")