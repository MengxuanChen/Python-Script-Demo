# import the necessary packages
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np 
import os
import sys

#Lead user to finish the facial enrollment
camera = PiCamera()
name = input("What's his/her Name? \n")
dirName = "./dataset/" + name
print(dirName)
if not os.path.exists(dirName):
    os.makedirs(dirName)
    print("Directory Created")
else:
    print("Name is taken")
    sys.exit()
readyEnroll = input("Please look at the camera and Type 'Yes' to start the enroll Process \n")
while True :
    if readyEnroll == 'Yes':
        print('Process Starts now')
        break
    else:
        readyEnroll = input("Please look at the camera and Type 'Yes' to start the enroll Process \n")
while True :
    #open a camera preview all the user see before taking a picture
    camera.start_preview(fullscreen=False, window=(100,20,480,320))
    for i in range(5):
        while True :
            isReady = input("Press 'A' to take a picture \n")
            if isReady == "a":
                camera.capture(dirName + "/" + name + str(i) + ".jpg")
                break
            else :
                isReady = input("Press 'A' to take a picture \n")
    #close the preview when the erollment is finished
    camera.stop_preview()
    break