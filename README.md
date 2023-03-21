# 💉🦠DOOM🦠💉

![Virus_Total_Analysis](https://user-images.githubusercontent.com/111704953/210577111-883e38da-55b1-4c14-be8d-dcd1c4bd1c5a.png)

## |Introduction:|

- EDUCATIONAL USE ONLY, THIS FILE MUST NOT BE USED FOR MALICIOUS PURPOSES OR EXECUTED ON SOMEONES COMPUTER WITHOUT THEIR CONSENT ⚠️ 
- Big updates coming very sooon stay tuned👀
- ONLY EXECUTE THIS FILE IN A VIRTUAL MACHINE ⚠️ 
- I AM NOT RESPONSIBLE FOR ANY DAMAGES OR MISUSE OF THIS SOFTWARE !
- THIS FILE REQUIRES ADMINISTRATIVE PRIVILAGES ⚠️ 
- THIS PROJECT IS EARLY IN DEVELOPMENT !
- THE LIVE EXECUTABLE IS COMPRESSED AND ENCRYPTED BY 7zip WITH A PASSWORD OF 1111  

---
## |Features:|
- My script tries to evade anaylysis and debugging.
- My script uses Zero third-party modules, only built in python modules.
- This script instantly disables detection by excluding c: drive.
- Installs and configures ssh-server on the target machine.
- Creates a new local administrator on the machine and hides it by changing the value of a UserList key.
- My script creates a hidden directory under %TEMP%\.0193 thats is where my executable deploys its resources.
- An amazing usb dropper has been implemented. The UsbDropper function copies the executable to all connected drives excluding the operating system drives.
- My script creates a txt document regarding time of execution and other system information located in %TEMP%\.0193\Log.txt.
---
## |Features i want to implement:|
- Everybrand of Anti-virus needs to be bypassed.
- Command and control Server connection.
- Remote Access Tool/Undetected reverse shell.
- Windows 11 Compatibility.
- Event logging functionality coming very soon.
- Undetected keylogging functionality super close to adoption.
- Screen shotting feature coming very soon.
---
## |Making it a windows executable:|
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
