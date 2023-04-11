import os, sys, urllib.request, time, zipfile
from BonkLib import Logging

Logging.StartUp(Tag='MLog')

print('Checking for ADB Requirements')
time.sleep(1)

if os.path.isfile('adb.exe'):
    Logging.Success('The ADB Requirements are already downloaded!\n Skipping.')
    time.sleep(2)
else:
    Logging.Warning("The ADB Requirements don't exist!\n Downloading...")
    time.sleep(5)
    url = 'https://cdn.discordapp.com/attachments/795101766425378856/1087570116151091231/Requirements.zip'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    try:
        awa = urllib.request.urlopen(req).read()
        try:
            with open('Requirements.zip', 'wb') as zipfiles:
                zipfiles.write(awa)
            with zipfile.ZipFile('Requirements.zip', 'r') as zip_ref:
                zip_ref.extractall()
            os.remove('Requirements.zip')
        except Exception as e:
            Logging.Error(e)
            Logging.Info('Failed to unzip Msg Cutie Lewko#4945\n The program will close in 5 seconds.')
            time.sleep(5)
            sys.exit()
    except Exception as e:
        Logging.Error(e)
        Logging.Info('ADB Requirements Failed to download please Msg Cutie Lewko#4945 on Discord!\n The program will close in 5 seconds.')
        time.sleep(5)
        sys.exit()

menu = """
1. MelonLog
2. Melonlog Debug

0. Exit
"""

def melonLog():
    mLogging = os.system('adb logcat -v time MelonLoader:D CRASH:D DEBUG:D *:S')
    Logging.info(mLogging)
    os.system('pause')

def melonlogDebug():
    mLoggingDebug = os.system('adb logcat -v time MelonLoader:D CRASH:D Mono:D mono:D mono-rt:D Zygote:D A64_HOOK:V DEBUG:D funchook:D Unity:D Binder:D AndroidRuntime:D *:S')
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