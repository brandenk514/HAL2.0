from picamera import PiCamera
from time import sleep
import datetime


class SecurityCamera:
    def __init__(self):
        self.camera = PiCamera()
        self.time = 10

    def get_file_name(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

    def start_recording(self):
        file_name = self.get_file_name()
        self.camera.start_recording('/home/pi/security_recordings/' + file_name + '.h264')
        sleep(self.time)
        self.camera.stop_recording()
