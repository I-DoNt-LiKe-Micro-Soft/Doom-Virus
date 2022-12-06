# 💉🦠DOOM🦠💉

![VIRUS_TOTAL_ANALYSIS](https://user-images.githubusercontent.com/111704953/205188043-88d5f412-9e03-46cf-a983-e1c5a662e78f.png)


## |Introduction:|

EDUCATIONAL USE ONLY AND I AM NOT RESPONSIBLE FOR ANY DAMAGES OR MISUSE OF THIS SOFTWARE !

Early in development this project is not complete or released !

This is my project to create a virus written in only python that will completely destroy you(theoretically) any help/suggestions is appreciated. It is hard to make an effective and undetectable python virus due to the lack of memory and cpu control i recommend c++ for ethical computer viruses. I am trying to make my script very noob friendly. I will also have a obfuscated live exe for you too test on a virtual machine or to try and deobfuscate goodluck with that.

---
## |Features:|
- My script uses Zero third-party modules, only built in python modules.
- This script instantly disables detection by excluding c: drive.
- Opens ports for ssh, reverse shell etc.
- Installs and configures ssh-server on the target machine.
- Creates a new user on the system for ssh.
- Moves exe and important files to temp folder.
- Hides the malware directory via the windows hide file attribute.
- USB Dropper has been implemented but needs improvement to exclude current working drive.
- Doom remover, reverses all changes and removes the virus.
---
## |Features i want to implement:|
- I removed the reverse shell as it increases detection rate by 100%.
- Everybrand of Anti-virus needs to be bypassed.
- C2 Server connection.
- Sensitive file enumeration and exfiltration.
- Crypto-mining functionalities if requested.
- Virtual machine detection
- I want my script to be able to spread over local area network.
- Im struggling to make the exe delete itself, i had it working at one point.
- Remote Access Tool/Undetected reverse shell
- I want to implement capabilities to spread over ssh. 
- Windows 11 Compatibility.
- Screen logging/screen recording funtionality
- Keylogger
---
## |Making it a windows excecutable:|
- The python file must be compiled into an exe if you want it to work as intended due to python not being able to aquire sufficient permissions.
- To make an exe you must use auto-py-to-exe https://pypi.org/project/auto-py-to-exe/
-On auto-py-to-exe you must enable the option under > Advanced > uac-admin this will correctly obtain administrator privilages.
 ```
pip install auto-py-to-exe
```
```
auto-py-to-exe
 ```
 ```
 pyinstaller --noconfirm --onefile --windowed --uac-admin  "C:/path_to_your_python_file.py"
 ```
![auto-py-to-exe_Usage](https://user-images.githubusercontent.com/111704953/194864233-b0e184c3-8814-4fe2-acdd-22132045a52f.png)
