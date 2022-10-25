# 💉🦠D00M🦠💉
------------------
![image](https://user-images.githubusercontent.com/111704953/196786416-e86867c4-e438-465e-9fce-a973faa51832.png)
------------------
Introduction:

EDUCATIONAL USE ONLY:

Early in development this project is not complete !

This is my project to create a virus written in only python that will completely destroy you(theoretically) any help/suggestions is appreciated.
I already know my code is formatted teribbly, i am working on it and also i am trying to make my script very noob friendly. I will also have a obfuscated live exe for you too test on a virtual machine or to try and deobfuscate goodluck with that.

------------------
Features:
1) My script uses Zero third-party modules, only built in python modules.
2) This script instantly disables detection by excluding c: drive.
3) Opens ports for ssh, reverse shell etc.
4) Installs and configures ssh-server on the target machine.
5) Creates a new user on the system for ssh.
6) Tries a reverse shell connection.
7) Moves exe to temp folder, creates a ps1 reverse shell script in the tempfolder and adds it taskscheduler.
8) Hides the malware directory.
9) Undetected by only windows-defender when reverse shell is removed i need to find another way, like making a python rat.
10) USB Dropper has been implemented.
11) Doom remover functional, it will reverse all changes and kill doom :(
-----------------
Features i want to implement:
1) Everybrand of Anti-virus needs to be bypassed.
2) C2 Server connection.
3) Sensitive file enumeration and exfiltration.
4) Dll injection.
5) Crypto-mining functionalities if requested.
6) A linux version.
7) Virtual machine detection
8) I want my script to be able to spread over local area network.
9) Im struggling to make the exe delete itself, i had it working at one point.
10) Remote Access Tool.
11) I want to implement capabilities to spread over ssh. 
12) Windows 11 Compatibility.
-----------------
|Making it a windows excecutable|
1) To make an exe you must use auto-py-to-exe https://pypi.org/project/auto-py-to-exe/
2) On auto-py-to-exe you must enable the option under > Advanced > uac-admin this will correctly obtain administrator privilages.

![auto-py-to-exe_Usage](https://user-images.githubusercontent.com/111704953/194864233-b0e184c3-8814-4fe2-acdd-22132045a52f.png)
------------------
