import time
import cv2
from paho.mqtt import client as mqtt_client

cam_port = 1
cam = cv2.VideoCapture(cam_port)
# vars to store current time and change in time
# previous_time = time()
# delta_time = 0
time.sleep(1)
result, image = cam.read() # reading input from camera
image_count = 0
while image_count < 7:
    result, image = cam.read()
    cv2.imshow("retest_image", image)
    cv2.imwrite("retest_image" + str(image_count) + ".png", image)
    time.sleep(0.25)
    image_count += 1
