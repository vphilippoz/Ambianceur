import RPi.GPIO as GPIO
import time
import pygame

# Configuration
MOTION_SENSOR_PIN = 17  # Signal pin of the motion sensor.
MUSIC_FOLDER = "/home/pi/music"  # Path to the music folder
MIN_PLAY_TIME = 300  # [s] Minimum playback time

# Global variables
music_playing = False
last_motion_time = 0 # [s]
start_time = 0 # [s] Time the music started playing

def initialize():
    """Set up GPIO and audio playback."""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)
    pygame.mixer.init() # Initialize the pygame mixer

def load_random_music():
    """Load a random music file from the music folder"""
    import os
    import random

    music_files = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")] #Or other formats
    if not music_files:
        print("No music files found in {}".format(MUSIC_FOLDER))
        return None

    music_file = random.choice(music_files)
    return os.path.join(MUSIC_FOLDER, music_file)

def play_music(music_file):
    """Play the specified music file."""
    global music_playing, start_time

    try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        music_playing = True
        start_time = time.time()
        print("Playing {}".format(music_file))
    except Exception as e:
        print("Error playing music: {}".format(e))

def stop_music():
    """Stop the music playback."""
    global music_playing
    pygame.mixer.music.stop()
    music_playing = False
    print("Stopping music")

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

            #Read the motion sensor
            motion = GPIO.input(MOTION_SENSOR_PIN)

            if motion:
                motion_detected()

            if music_playing:
                #Check if music should be stopped
                elapsed_time = time.time() - last_motion_time
                total_play_time = time.time() - start_time

                if elapsed_time > 1 and total_play_time > MIN_PLAY_TIME : #No motion during 1 second, minimum play time reached.
                    stop_music()
            else:
                #If no music is playing, check if motion is detected
                if time.time() - last_motion_time < 1: #Motion during the last second
                    music_file = load_random_music()
                    if music_file:
                        play_music(music_file)

            time.sleep(0.1) #Short delay

    except KeyboardInterrupt:
        print("Exiting program")
    finally:
        GPIO.cleanup() #Clean up GPIO on exit
        pygame.mixer.quit()

if __name__ == "__main__":
    initialize()
    main_loop()
