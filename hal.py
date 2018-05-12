import motion_sensor

class Hal:
    def __init__(self):
        self.motion_sensor = motion_sensor.MotionSensor()
        hal.motion_sensor.run_motion_sensor()

if __name__ == '__main__':
    hal = Hal()
