#----- A simple TCP client program in Python using send() function -----

import socket
import re
import numpy as np
import cv2
from matplotlib import pyplot as plt
import argparse

def run(
        live=False,  # is the system connected to live feed
):
    ## USER DEFINED VALUES
    # IRL REFERENCE FOR IMAGE
    env_dim = [1, 0.5]
    # IMAGE SIZE
    img_dim = [3840, 2160]

    if live:
        # CALL CLIENT TO GET COORDINATES
        try:
            data = client() # x, y, w, h, c
            # CALCULATE MOVE DISTANCE
            movement = getDistance(img_dim, env_dim, (img_dim[0]/2, img_dim[1]/2), (data[0]*img_dim[0], data[1]*img_dim[1]))
            print(movement[0], movement[1])
            return movement
        except ConnectionRefusedError:
                print("[Errno 111] Connection refused")

    else:
        show_bbox(0.745833, 0.139352, 0.0270833, 0.0481481)

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
    # print("decoded:"+dec)
    m = p.match(dec)
    x = m.group(1) # x
    y = m.group(2) # y
    w = m.group(3) # width of bounding box
    h = m.group(4) # height of bounding box
    c = m.group(5) # confidence
    # print("x:"+x)
    # print("w:"+w)

    # Send data to server
    data = "Pose received!";

    clientSocket.send(data.encode());

    return float(x), float(y), float(w), float(h), float(c)

def calc(ImageDim, EnvDim, Point):
    return (Point[0] * EnvDim[0]/ImageDim[0], Point[1] * EnvDim[1]/ImageDim[1])

def getDistance(img_dim, env_dim, point1, point2):
    """
    img_dim = image WxH (pixel values)
    env_dim = IRL reference WxH (m or mm)
    point1 = middle of ws (pixel values)
    point2 = found cell (pixel values)

    returns:
    dist_x = point2 X coordinate distance from point1
    dist_y = point2 Y coordinate distance from point1
    """

    conv_point1 = calc(img_dim, env_dim, point1) #img_dim = (w,h), env_dim = (w, h) in meters/mm
    # print(conv_point1)
    conv_point2 = calc(img_dim, env_dim, point2)
    # print(conv_point2)

    dist_x = np.sqrt((conv_point1[0] - conv_point2[0])**2)
    dist_y = np.sqrt((conv_point1[1] - conv_point2[1])**2)

    if point2[0] < point1[0]:
        dist_x = dist_x * (-1)

    if point2[1] < point1[1]:
        dist_y = dist_y * (-1)

    print(dist_x,dist_y)

    return dist_x, dist_y

def show_bbox(x, y, w, h):
    img = cv2.imread('/home/oskars/workspace/learn_ws/src/edi_rovam_yolov7/test1.jpg')

    dh, dw, _ = img.shape # 2160, 3840
    # print(dh, dw)

    l = int((x - w / 2) * dw)
    r = int((x + w / 2) * dw)
    t = int((y - h / 2) * dh)
    b = int((y + h / 2) * dh)

    cx = x*dw
    cy = y*dh
    # print(cx, cy)

    getDistance((dw, dh), (1, 0.5), (dw/2, dh/2), (cx, cy))
    
    if l < 0:
        l = 0
    if r > dw - 1:
        r = dw - 1
    if t < 0:
        t = 0
    if b > dh - 1:
        b = dh - 1

    # print(l,r,t,b)

    cv2.rectangle(img, (l, t), (r, b), (255, 0, 0), 5)
    cv2.circle(img, (int(cx),int(cy)), radius=5, color=(0, 255, 0), thickness=-1)
    cv2.circle(img, (int(dw/2),int(dh/2)), radius=5, color=(255, 255, 0), thickness=-1)

    plt.imshow(img)
    plt.show()    

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--live', action='store_true', help='is the system connected to live feed')
    opt = parser.parse_args()
    return opt

def main(opt):
    run(**vars(opt))

if __name__ == "__main__":
    opt = parse_opt()
    main(opt)