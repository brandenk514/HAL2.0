from picamera import PiCamera
from time import sleep
import datetime
import os
import time
from sys import argv


class SecurityCamera:
    def __init__(self):
        self.camera = PiCamera()
        self.time = 10

    def get_file_name(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

    def start_recording(self):
        file_name = self.get_file_name()
        self.camera.rotation = 180
        self.camera.start_recording('/home/branden/camera/security_recordings/' + file_name + '.h264')
        sleep(self.time)
        self.camera.stop_recording()
