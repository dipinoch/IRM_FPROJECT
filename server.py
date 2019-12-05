
import sys
sys.path.append('/usr/local/lib')
import socket
import time
from imutils.video import VideoStream
from imagezmq import ImageSender

sender = ImageSender(connect_to='tcp://127.0.0.1:5555')
cam_name = socket.gethostname() 
cam = VideoStream(src=0).start()
time.sleep(2.0)  
while True:  # send images as stream until Ctrl-C
    image = cam.read()
    sender.send_image(cam_name, image)