# coding: utf-8
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(1200)
camera.stop_preview()
