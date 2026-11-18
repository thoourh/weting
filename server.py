from socket import *

serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind(('',8080))
serverSock.listen(1)
isContinue = True
ConnectionSock, addr = serverSock.accept()
print("Connection established with: ", str(addr))
while(isContinue):
    
    data = ConnectionSock.recv(1024)
    print("Message recevied from client: ", data.decode('utf-8'))

    msg = input("Enter the msg: ")

    ConnectionSock.send(msg.encode('utf-8'))
    print("Message sent to  client")

    print("connection keep going?")
    
    choice = True
    while(choice):
        ss = input("Enter Y/N: ")
        if ss=="Y":
            isContinue = True
            choice = False
        elif ss=="N":
            isContinue = False
            choice = False
        else:
            choice = True
            



