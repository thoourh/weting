from socket import *
from threading import *

serverSock = socket(AF_INET,SOCK_STREAM)
serverSock.bind(('',8080))
serverSock.listen(1)
isContinue = True
ConnectionSock, addr = serverSock.accept()
print("Connection established with: ", str(addr))

isContinue = True

def recvMsg():
    global isContinue
    while(isContinue):
        data = ConnectionSock.recv(1024)
        if not data:
            print("Client disconnected")
            isContinue = False
            break
        print(f"\rMessage received from server: {data.decode('utf-8')}")

def sendMsg():
    global isContinue
    while(isContinue):
        msg = input("Enter the msg: ")
        if msg == "exit":
            isContinue = False
            break
        ConnectionSock.send(msg.encode('utf-8')) 

    ConnectionSock.close()
    serverSock.close()
            

    
t1 = Thread(target=recvMsg, daemon=True)
t2 = Thread(target=sendMsg)
    
t1.start()
t2.start()
    
t2.join()
print("Chat ended.")

