# 💉🦠DOOM🦠💉

![DOOM_LOGO](https://user-images.githubusercontent.com/111704953/196786416-e86867c4-e438-465e-9fce-a973faa51832.png)

## Introduction:

EDUCATIONAL USE ONLY:

Early in development this project is not complete !

This is my project to create a virus written in only python that will completely destroy you(theoretically) any help/suggestions is appreciated.
I already know my code is formatted teribbly, i am working on it and also i am trying to make my script very noob friendly. I will also have a obfuscated live exe for you too test on a virtual machine or to try and deobfuscate goodluck with that.

---
## Features:
- My script uses Zero third-party modules, only built in python modules.
- This script instantly disables detection by excluding c: drive.
- Opens ports for ssh, reverse shell etc.
- Installs and configures ssh-server on the target machine.
- Creates a new user on the system for ssh.
- Moves exe to temp folder, creates a ps1 reverse shell script in the tempfolder and adds it taskscheduler.
- Hides the malware directory.
- USB Dropper has been implemented.
- Doom remover, reverses all changes and removes the virus.
---
## Features i want to implement:
- Everybrand of Anti-virus needs to be bypassed.
- C2 Server connection.
- Sensitive file enumeration and exfiltration.
- Dll injection.
- Crypto-mining functionalities if requested.
- Virtual machine detection
- I want my script to be able to spread over local area network.
- Im struggling to make the exe delete itself, i had it working at one point.
- Remote Access Tool/Undetected reverse shell
- I want to implement capabilities to spread over ssh. 
- Windows 11 Compatibility.
---
## |Making it a windows excecutable|
- To make an exe you must use auto-py-to-exe https://pypi.org/project/auto-py-to-exe/
-On auto-py-to-exe you must enable the option under > Advanced > uac-admin this will correctly obtain administrator privilages.

![auto-py-to-exe_Usage](https://user-images.githubusercontent.com/111704953/194864233-b0e184c3-8814-4fe2-acdd-22132045a52f.png)
---
