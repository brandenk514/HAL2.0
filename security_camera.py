from picamera import PiCamera
from time import sleep
import datetime


class SecurityCamera:
    def __init__(self):
        self.camera = PiCamera()

    def get_file_name(self):
        return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

    def start_recording(self, seconds):
        file_name = self.get_file_name()
        self.camera.start_preview()
        self.camera.start_recording('/home/pi/security_recordings/' + file_name + ' %d.h264')
        sleep(seconds)
        self.camera.stop_recording()
        self.camera.stop_preview()


if __name__ == '__main__':
    c = SecurityCamera()
    c.start_recording()
