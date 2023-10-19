#----- A simple TCP based server program in Python using send() function -----

import socket

# Create a stream based socket(i.e, a TCP socket)

# operating on IPv4 addressing scheme

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Bind and listen

serverSocket.bind(("127.0.0.1",9090)); # for local-host
# serverSocket.bind(("10.13.137.147",9090));

serverSocket.listen();

# Accept connections

while(True):
    print("started server")

    (clientConnected, clientAddress) = serverSocket.accept();

    print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]));

    clientConnected.send("(0.1,0.2,0.3,0.4)".encode());

    dataFromClient = clientConnected.recv(1024)

    print("Response: "+dataFromClient.decode());
  