from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM

class Server:
    def __init__(self):
        self.host = "localhost"
        self.port = 9090
        self.NEWSOCKET = socket(AF_INET, SOCK_STREAM) #-Create a new socket using the given address family, socket type and protocol number.
        
    def Connect(self):
        self.NEWSOCKET.bind((self.host, self.port)) #-We use bind for the server and connect for the client.
        self.NEWSOCKET.listen(5) #-Listen specifies how many failed connections we accept before rejecting new ones.
        self.CommunicationSocket, address = self.NEWSOCKET.accept() #-The accept method waits for connections.When a client connects it returns the address of the client and the socket we can use too communicate.
        print(f"[*]Receiving connection from: {address}\n")

    def Communicate(self, UserInput):
        self.UserInput = input("[*]Enter your option: ").encode("utf-8")
        if UserInput.decode("utf-8") in ["1"]:
            self.CommunicationSocket.send(UserInput)
            self.CommunicationSocket.send(input("[*]Command: ").encode("utf-8"))
            print(self.CommunicationSocket.recv(403925).decode("utf-8"))
            
def main():
    MyObj = Server()
    MyObj.Connect()
    while(True):
        MyObj.Communicate(input("[*]Enter your option: ").encode("utf-8"))
    MyObj.CommunicationSocket.close()
    print("[!]Connection closed!")
main()

#message = self.CommunicationSocket.recv(1024).decode("utf-8") #-Receive buffer
#self.CommunicationSocket.send("shutdown /s".encode("utf-8"))
