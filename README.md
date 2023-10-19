# Installation instructions for WINDOWS

### Install Python and YOLOv7

https://wandb.ai/onlineinference/YOLO/reports/YOLOv5-Object-Detection-on-Windows-Step-By-Step-Tutorial---VmlldzoxMDQwNzk4

1. Download and install >=3.8 version of Python from https://www.python.org/downloads/
1.1. Test if it's working. In windows explorer go to the Python directory (C:\Users\user\AppData\Local\Programs\Python) 
1.2. In the address bar write **cmd** to open a terminal. Then write **python** and press enter.

2. Install PyTorch. In https://pytorch.org/get-started/locally/ set the STABLE, WINDOWS, PIP, PYTHON, CPU version.
2.1. Open the python scripts folder ((C:\Users\user\AppData\Local\Programs\Python\Python3\Scripts)
2.2. In address bar write **cmd**
2.3. Run the **pip** command in the terminal

3. Install YOLOv7
3.1. Go to edi_rovam_yolov7 folder and in address bar write **cmd**
3.2. Install the requirements
```
pip install -r requirements.txt
```
3.3. In case of large red error, install Visual Studio from https://visualstudio.microsoft.com/downloads/

# Running the programe
The system is made with the idea in mind, that the client is ran through a LabView programme, using the Python Integration Toolkit (http://docs.enthought.com/python-for-LabVIEW/guide/install.html)

### Segmentation
To launch the segmentation, in edi_rovam_yolov7/added_code run
```
python server_detect.py --source 0 --send_to_server
```
It is set to send the found coordinates to local_host. For a different IP, change it in line 
```
serverSocket.bind(("127.0.0.1",9090));
```
### Client
To receive the coordinates, in edi_rovam_yolov7/added_code run
```
python client.py
```
It is set to receive coordinates from local_host. For a diferrent IP, change in in line
```
server_ip = "127.0.0.1"
```
