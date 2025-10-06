import RPi.GPIO as GPIO
import parameters as p

def initialize() -> None:
    """
    Initialize the motion sensor.
    """
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(p.MOTION_SENSOR_PIN, GPIO.IN)

def finalize() -> None:
    """
    Finalize the motion sensor.
    """
    GPIO.cleanup()

def read_motion_sensor() -> bool:
    """
    Read the motion sensor.

    Return true if motion is detected, false otherwise.
    """
    return GPIO.input(p.MOTION_SENSOR_PIN)

# def motion_handler() -> None:
#     """
#     Handle motion detection.
#     """
#     global last_motion_time
#     last_motion_time = time.time()

#     if p.VERBOSE: print("Motion Detected!")
