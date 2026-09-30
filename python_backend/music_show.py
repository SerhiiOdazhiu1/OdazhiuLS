import sys
import os
import time
import numpy as np
import sounddevice as sd

os.environ['PATH'] = r"C:\EDIABAS\bin;" + os.environ.get('PATH', '')
if hasattr(os, 'add_dll_directory'):
    try:
        os.add_dll_directory(r"C:\EDIABAS\bin")
    except Exception:
        pass

from pydiabas import PyDIABAS
from bmw_moduls import get_module_for_chassis

CHUNK = 1024
RATE = 44100
BASS_MAX_FREQ = 140

freqs = np.fft.rfftfreq(CHUNK, 1.0 / RATE)
bass_mask = freqs < BASS_MAX_FREQ


def get_bass_volume(indata):
    mono = np.mean(indata, axis=1)
    fft_data = np.fft.rfft(mono)
    bass_fft = np.abs(fft_data[bass_mask])
    return np.mean(bass_fft)


def run_music_show(chassis):
    current_threshold = 25.0
    last_file_read = 0.0

    print("[*] Connecting to EDIABAS...")

    try:
        with PyDIABAS() as bmw:
            with sd.InputStream(samplerate=RATE, channels=1, blocksize=CHUNK) as stream:
                module = get_module_for_chassis(chassis, bmw)
                module.connect()

                while True:
                    now = time.time()
                    if now - last_file_read > 0.5:
                        try:
                            with open("threshold.txt", "r") as f:
                                content = f.read().strip()
                                if content:
                                    current_threshold = float(content)
                        except:
                            pass
                        last_file_read = now

                    data, overflowed = stream.read(CHUNK)
                    bass_vol = get_bass_volume(data)

                    bar_length = int(min(bass_vol * 0.8, 50))
                    bar = "#" * bar_length

                    if bass_vol > current_threshold:
                        print(f"\r[ Бас ] {bar:<50} (Vol: {bass_vol:.1f})", end="", flush=True)

                        module.music_beat()
                        time.sleep(module.cooldown)

                        stream.read(stream.read_available)
                    else:
                        print(f"\r[     ] {bar:<50} (Vol: {bass_vol:.1f})", end="", flush=True)

    except KeyboardInterrupt:
        print("\n\n The music show has been stopped.")
        try:
            with PyDIABAS() as bmw:
                module = get_module_for_chassis(chassis, bmw)
                module.stop()
        except:
            pass
    except Exception as e:
        print(f"\n Critical error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error!")
        input("Press Enter to exit.")
        sys.exit(1)

    chassis = sys.argv[1]

    if len(sys.argv) >= 3 and sys.argv[2].lower() == "stop":
        try:
            with PyDIABAS() as bmw:
                module = get_module_for_chassis(chassis, bmw)
                module.stop()
        except:
            pass
        sys.exit(0)

    run_music_show(chassis)
