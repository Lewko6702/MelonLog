import os
import sys

from BonkLib import Logging

menu = """
1. MelonLog
2. Melonlog Debug

0. Exit
"""

def melonLog():
    mLogging = os.system('adb logcat -v time MelonLoader:D CRASH:D DEBUG:D *:S')
    Logging.StartUp(Tag='MLOG')
    Logging.info(mLogging)
    os.system('pause')

def melonlogDebug():
    mLoggingDebug = os.system('adb logcat -v time MelonLoader:D CRASH:D Mono:D mono:D mono-rt:D Zygote:D A64_HOOK:V DEBUG:D funchook:D Unity:D Binder:D AndroidRuntime:D *:S')
    Logging.StartUp(Tag='MLOGDebug')
    Logging.info(mLoggingDebug)

while True:
    try:
        print(menu)
        a = int(input('Choose an option: '))
        match a:
             case 0:
                print("Exiting program...")
                sys.exit()
             case 1:
                melonLog()
             case 2:
                melonlogDebug()

             case _:
                print('Invalid option please choose a valid option.')
    except ValueError:
        print("Invalid input please enter a number.")