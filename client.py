from socket import *
from threading import *
clientSock = socket(AF_INET, SOCK_STREAM)
ip_address = input("Enter the server IP address: ")
isContinue = True
clientSock.connect((ip_address,8080))

print("Connected to server")

def recvMsg():
    global isContinue
    while(isContinue):
        data = clientSock.recv(1024)
        if not data:
            print("Server disconnected")
            isContinue = False
            break
        print(f"\rMessage received from server: {data.decode('utf-8')}")

def sendMsg():
    global isContinue
    while(isContinue):
        msg = input("Enter the msg to send to server: ")
        if msg == "exit":
            isContinue = False
            break
        clientSock.send(msg.encode('utf-8'))

    clientSock.close()
    
    
t1 = Thread(target=recvMsg, daemon=True)
t2 = Thread(target=sendMsg)
    
t1.start()
t2.start()

t2.join()
print("Chat ended.")

