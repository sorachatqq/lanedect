import picamera
from picamera.array import PiRGBArray
import numpy as np
import cv2
import time
import warnings
import serial
warnings.filterwarnings('error')

image_size=(320, 192)
camera = picamera.PiCamera()
camera.resolution = image_size
camera.framerate = 50
camera.vflip = False
camera.hflip = False
#camera.exposure_mode='off'
rawCapture = PiRGBArray(camera, size=image_size)
arduinoSerialData = serial.Serial('/dev/ttyUSB0',9600)
