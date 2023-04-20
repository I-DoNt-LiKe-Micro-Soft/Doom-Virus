# Generator
$command = 'POWERSHELL COMMAND YOU WANT ENCODING GOES HERE'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$base64 = [Convert]::ToBase64String($bytes)

# Launcher
Write-Host "---------------------------------------------------------"
Write-Host "Github:  https://github.com/I-DoNt-LiKe-Micro-Soft/Doom"
[System.Environment]::NewLine
Write-Host "$ - Your base64 encoded powershell command is below !"
[System.Environment]::NewLine
Write-Host "powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc '$base64'"
Write-Host "---------------------------------------------------------"
