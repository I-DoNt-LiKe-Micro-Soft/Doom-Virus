#!/usr/bin/env python3

import ctypes
import sys
import time
import os
import subprocess



def is_usr_admin(): #_Checks_If_Script_Has_Admin_Privs
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("ERROR")
        ctypes.windll.shell32.ShellExecuteW(
            None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
        exit(0)
    else:
        time.sleep(0.5)
is_usr_admin()

current_user = os.getenv('username')
mal_dir = "C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923"

def shell_commands():
    subprocess.run('powershell.exe Unregister-ScheduledTask -TaskName "SYSTEM32"')
    time.sleep(0.2)
    subprocess.run('powershell.exe Remove-MpPreference -ExclusionPath “C:”', shell=True)
    time.sleep(0.2)
    subprocess.run('powershell.exe Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope LocalMachine -Force', shell=True)
    time.sleep(0.2)
    subprocess.run('powershell.exe Remove-NetFirewallRule -DisplayName "VIRUS"', shell=True)
    time.sleep(0.2)
    subprocess.run("powershell.exe Set-Service -Name sshd -StartupType 'Manual'", shell=True)
    time.sleep(0.2)
    subprocess.run("powershell.exe Remove-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0", shell=True)
    time.sleep(0.2)
    subprocess.run('powershell.exe Remove-LocalGroupMember -Group "Administrators" -Member "defaultuser"', shell=True)
shell_commands()

try:
    os.rmdir("" + mal_dir + "")
except:
    print("TMP_FOLDER_ALREADY_GONE")

ctypes.windll.user32.MessageBoxW(0, "DOOM_REMOVED_AND_ALL_SETTINGS_REVERTED----Please_Report_Any_Errors_On_Github", "SUCCESS", 1)

