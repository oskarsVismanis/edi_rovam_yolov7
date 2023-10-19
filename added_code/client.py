#----- A simple TCP client program in Python using send() function -----

import socket
import re
# from PySharedVariables import SharedVariables

def client():

    # Create a client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    p = re.compile(r"^\((.*),(.*),(.*),(.*),(.*)\)$") # match 5 strings with format (d.ddd,d.ddd,d.ddd,d.ddd,d.ddd)

    # Connect to the server
    # server_ip = "10.13.137.147"#"10.13.137.57"
    server_ip = "127.0.0.1" #for local host

    clientSocket.connect((server_ip,9090)); 

    dataFromServer = clientSocket.recv(1024);

    # Print to the console
    dec = dataFromServer.decode();
    print("decoded:"+dec)
    m = p.match(dec)
    x = m.group(1) # x
    y = m.group(2) # y
    w = m.group(3) # width of bounding box
    h = m.group(4) # height of bounding box
    c = m.group(5) # confidence
    print("x:"+x)
    print("w:"+w)

    # Send data to server
    data = "Pose received!";

    clientSocket.send(data.encode());

    return float(x), float(y), float(w), float(h), float(c)

# def sendToLabView(data):
#     host = "127.0.0.1"
#     port = 9091

#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((host, port))
#     # data = []
#     s.sendall(str(data).encode())

def calculateCentre(x, y, w, h):

    centre = [0 for i in range (2)]
    centre[0] = x + w/2
    centre[1] = y + h/2

    return centre

def main():
    x, y, w, h, c = client()

    centre = calculateCentre(x,y,w,h)

    print("Centre of cell is [x: "+str(centre[0])+", y: "+str(centre[1])+"]")

if __name__ == "__main__":
    main()