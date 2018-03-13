import RPi.GPIO as GPIO
import security_camera


class MotionSensor:
    def __init__(self):
        self.camera = security_camera.SecurityCamera()

    def run_motion_sensor(self):
        PIR = 4
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(PIR, GPIO.IN, GPIO.PUD_DOWN)
        try:
            print("Turning on motion sensor...")

            # Loop until PIR indicates nothing is happening
            while GPIO.input(PIR) == 1:
                Current_State = 0

            print("Sensor ready")

            while True:
                print('Waiting for movement')
                GPIO.wait_for_edge(PIR, GPIO.RISING)
                print('Movement detected')
                security_camera.SecurityCamera.start_recording(self.camera)

        except KeyboardInterrupt:
            print("Bye for now")
            # Reset GPIO
            GPIO.cleanup()
