from time import strftime
from time import gmtime
from socket import gethostname
from platform import processor
from platform import platform
from platform import system
from platform import release
from platform import version
from platform import machine
from platform import win32_edition
from platform import architecture

def Logging(): #The log gets saved in the temp directory
    HOSTNAME = gethostname()
    HOSTNAMESTRING = HOSTNAME
    with open(environ['temp']+"\\Log.txt", "w") as LogFile:
        LogFile.write("Date of execution(GMT): "+strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())+"\n")
        LogFile.write("Hostname: "+HOSTNAMESTRING+"\n")
        LogFile.write("Username: "+environ['username']+"\n")
        LogFile.write("Architecture: "+architecture()[0]+"\n")
        LogFile.write("Processor: "+processor()+"\n")
        LogFile.write("System: "+system()+"\n")
        LogFile.write("Platform: "+platform()+"\n")
        LogFile.write("Release: "+release()+"\n")
        LogFile.write("Version: "+version()+", "+version().split('.')[2]+"\n")
        LogFile.write("Machine: "+machine()+"\n")
        LogFile.write("Edition: "+win32_edition()+"\n")
        LogFile.close()


Logging()