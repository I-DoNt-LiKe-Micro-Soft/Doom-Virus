# Generator
$Command = 'THE COMMAND YOU WOULD LIKE TO REVERSE GOES HERE'.ToCharArray()
$Reversed = @()
($Command.length - 1)..0 | ForEach-Object {
    $Reversed += $Command[$_]
}
$Reversed = $Reversed -join ''
Write-Host "-------------------------------"
Write-Host "Github:  https://github.com/I-DoNt-LiKe-Micro-Soft/Doom"
Write-Host "Your Reversed PowerShell Command Is Below Please Use The Launcher That Can Be Found At The Bottom Of This File."
[System.Environment]::NewLine
Write-Host $Reversed
Write-Host "-------------------------------"


# Launcher Below Remove Hashtags!

# $Reversed = 'YOUR REVERSED COMMAND GOES HERE'
# $Normal = @()
# ($Reversed.length - 1)..0 | ForEach-Object {
#     $Normal += $Reversed[$_]
# }
# $Normal = $Normal -join ''
# Invoke-Expression $Normal