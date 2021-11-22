from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

# print("This is coded message"[::-1]) # Secret coded msg, just for you :)

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime('%d-%m-%Y_%H-%M-%S')
file_name = (f"{time_stamp}.mp4")

venv = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, venv, 20.0, (width, height))

#webcam = cv2.VideoCapture(0) # To use webcam uncomment this

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    #_, frame = webcam.read() # To use webcam uncomment this
    #fr_height, fr_width, _ = frame.shape # To use webcam by overlaying uncomment this
    # img_final[0: fr_height, 0: fr_width, :] = frame[0: fr_height, 0: fr_width, :] # To use webcam by overlaying uncomment this
    #cv2.imshow('WebCam', frame)

    cv2.imshow('Screen Recording', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(1) == ord('q'):
        break