import os
import platform
import subprocess

def sleep_laptop():
    system_platform = platform.system()

    if system_platform == "Windows":
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif system_platform == "Linux":
        subprocess.run(["systemctl", "suspend"])
    elif system_platform == "Darwin":
        os.system("pmset sleepnow")
    else:
        print("Unsupported operating system for sleep operation.")

if __name__ == "__main__":
    sleep_laptop()
