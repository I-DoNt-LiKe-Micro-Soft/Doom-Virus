# 💉🦠DOOM🦠💉


![virus_total_analysis](https://user-images.githubusercontent.com/111704953/210521079-59d4aefa-6b5a-4df5-856d-49d780fefcc8.png)


## |Introduction:|

EDUCATIONAL USE ONLY AND I AM NOT RESPONSIBLE FOR ANY DAMAGES OR MISUSE OF THIS SOFTWARE !

This project is early in development.

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
- My script hides the new created user system wide.
---
## |Features i want to implement:|
- I want my script to create a txt file with data regarding time of infection and other user details.
- Big changes coming soon to decrease detection rate, this may include Doom dropping powershell scripts, wish me luck.
- I removed the reverse shell as it increases detection rate by 100%.
- Everybrand of Anti-virus needs to be bypassed.
- Command and control Server connection.
- Virtual machine detection and evasion.
- Remote Access Tool/Undetected reverse shell
- Windows 11 Compatibility.
- Screen Logging functionality coming very soon.
- Keylogger
---
## |Making it a windows excecutable:|
- The python file must be compiled into an exe if you want it to work as intended due to python not being able to aquire sufficient permissions.
- To make an exe you must use auto-py-to-exe https://pypi.org/project/auto-py-to-exe/
-On auto-py-to-exe you must enable the option under > Advanced > uac-admin this will correctly obtain administrator privilages.
 ```
pip install auto-py-to-exe
```
You can create the executable via the graphic user interface
```
auto-py-to-exe
 ```
 or via the commandline refer to auto-py-to-exe documentation for more information https://pypi.org/project/auto-py-to-exe/
 ```
 pyinstaller --noconfirm --onefile --windowed --uac-admin  "C:/path_to_your_python_file.py"
 ```
![auto-py-to-exe_Usage](https://user-images.githubusercontent.com/111704953/194864233-b0e184c3-8814-4fe2-acdd-22132045a52f.png)
