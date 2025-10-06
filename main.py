import RPi.GPIO as GPIO
import time
import parameters as p
import music

# Global variables
music_playing = False
last_motion_time = 0 # [s]
start_time = 0 # [s] Time the music started playing

def initialize():
    """Set up GPIO and audio playback."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(p.MOTION_SENSOR_PIN, GPIO.IN)

    music.initialize()

def motion_detected():
    """Handle motion detection."""
    global last_motion_time
    last_motion_time = time.time()
    print("Motion Detected!")

def main_loop():
    """Main program loop."""
    global music_playing, last_motion_time, start_time

    try:
        while True:
            # Read the motion sensor
            motion = GPIO.input(p.MOTION_SENSOR_PIN)

            if motion:
                motion_detected()

            if music_playing:
                # Check if music should be stopped
                elapsed_time = time.time() - last_motion_time
                total_play_time = time.time() - start_time

                if elapsed_time > 1 and total_play_time > p.MIN_PLAY_TIME : # No motion during 1 second, minimum play time reached.
                    music.stop()
            else:
                # If no music is playing, check if motion is detected
                if time.time() - last_motion_time < p.PERIOD: # Motion during the last second
                    music_file = music.load()
                    if music_file:
                        music.play(music_file)

            time.sleep(p.PERIOD) #Short delay

    except KeyboardInterrupt:
        print("Exiting program")
    finally:
        GPIO.cleanup() # Clean up GPIO on exit
        music.finalize()

if __name__ == "__main__":
    initialize()
    main_loop()
