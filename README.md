# DooM-Virus
------------------
Introduction:

Early in development this project is not complete.

This is my project to create a virus written in only python that will completely destroy you(theoretically) any help/suggestions is appreciated.
I already know my code is formatted teribbly, i am working on it and also i am trying to make my script very noob friendly. I will also have a obfuscated live exe for you too test on a virtual machine or to try and deobfuscate goodluck with that.

------------------
features:
1) My script uses Zero third-party modules, only built in python modules.
2) So far Undetected by ONLY windows defender, my script instantly disables detection by excluding c: drive.
3) Opens ports for ssh, reverse shell etc.
4) Installs and configures ssh-server on the target machine.
5) Creates a new user on the system for ssh.
6) Tries a reverse shell connection.
7) Moves exe to temp folder, creates a ps1 reverse shell script in the tempfolder and adds it to startup with a batchscript.
8) Hides the malware directory.
9) Then deletes the exe from the system relying on the reverse shell startup script for persistence
-----------------
|Making it a windows excecutable|
1) To make an exe you must use auto-py-to-exe https://pypi.org/project/auto-py-to-exe/
2) On auto-py-to-exe you must enable the option under > Advanced > uac-admin this will correctly obtain administrator privilages.
![auto-py-to-exe_Usage](https://user-images.githubusercontent.com/111704953/194864233-b0e184c3-8814-4fe2-acdd-22132045a52f.png)
------------------
