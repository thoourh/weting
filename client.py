from socket import *
clientSock = socket(AF_INET, SOCK_STREAM)
ip_address = input("Enter the server IP address: ")
isContinue = True
clientSock.connect((ip_address,8080))

print("Connected to server")
while(isContinue):
    msg = input("Enter the msg to send to server: ")
    if msg == "exit":
        isContinue = False
        break
    clientSock.send(msg.encode('utf-8'))
    
    print("Message sent to server")

    data = clientSock.recv(1024)
    print("Message received from server: ", data.decode('utf-8'))


