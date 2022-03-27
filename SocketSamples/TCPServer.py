from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
connectionSocket, addr = serverSocket.accept()
print("connect from:", addr)

while True:
    message = connectionSocket.recv(1024).decode()
    print(message)
    modifiedMessage = message.upper()
    connectionSocket.send(modifiedMessage.encode())

connectionSocket.close()