#WARNING: Issues detected with network drives!
#I would like to increase the artificial intelligence of the screenshotter.
Add-Type -AssemblyName System.Windows.Forms,System.Drawing
$screens = [Windows.Forms.Screen]::AllScreens
$top    = ($screens.Bounds.Top    | Measure-Object -Minimum).Minimum
$left   = ($screens.Bounds.Left   | Measure-Object -Minimum).Minimum
$width  = ($screens.Bounds.Right  | Measure-Object -Maximum).Maximum
$height = ($screens.Bounds.Bottom | Measure-Object -Maximum).Maximum
$bounds   = [Drawing.Rectangle]::FromLTRB($left, $top, $width, $height)
$bmp      = New-Object System.Drawing.Bitmap ([int]$bounds.width), ([int]$bounds.height)
$graphics = [Drawing.Graphics]::FromImage($bmp)
$graphics.CopyFromScreen($bounds.Location, [Drawing.Point]::Empty, $bounds.size)
#$Path = "$pwd\"
while($True){
    $Count = 0
    while($True){
        $Count++
        $bmp.Save("${Count}.png")
        if(1000 -eq $Count){break;}
    }
    Remove-Item *.png
}
$graphics.Dispose()
$bmp.Dispose()
