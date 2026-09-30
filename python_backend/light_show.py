import sys
import os


os.environ['PATH'] = r"C:\EDIABAS\bin;" + os.environ.get('PATH', '')

if hasattr(os, 'add_dll_directory'):
    try:
        os.add_dll_directory(r"C:\EDIABAS\bin")
    except Exception:
        pass

import time
from pydiabas import PyDIABAS
from bmw_moduls import get_module_for_chassis

ON_TIME = 0.1
OFF_TIME = 0.03
CYCLES = 8

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error")
        input("Press Enter to exit.")
        sys.exit(1)

    chassis = sys.argv[1]

    if len(sys.argv) >= 3 and sys.argv[2].lower() == 'stop':
        try:
            with PyDIABAS() as bmw:
                module = get_module_for_chassis(chassis, bmw)
                module.stop()
        except:
            pass
        sys.exit(0)

    try:
        with PyDIABAS() as bmw:
            try:
                module = get_module_for_chassis(chassis, bmw)
                module.connect()
                module.lights_show_run(CYCLES, OFF_TIME, ON_TIME)

            except KeyboardInterrupt:
                module = get_module_for_chassis(chassis, bmw)
                module.stop()
                print("\n Stopped via interface (Stop)")
            except Exception as inner_e:
                print(f"\n Error during the show: {inner_e}")
            finally:
                try:
                    module = get_module_for_chassis(chassis, bmw)
                    module.stop()
                except:
                    pass
    except Exception as e:
        print(f"\n Critical error connecting to EDIABAS: {e}")
