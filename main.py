import time
import parameters as p
import music, sensor

# Global variables
music_playing = False
start_time = 0 # [s] Time the music started playing

def initialize() -> None:
    """
    Set up motion detection and audio playback.
    """
    sensor.initialize()
    music.initialize()


def main_loop() -> None:
    """
    Main program loop.
    """
    global music_playing, start_time

    start_music: bool = False
    last_motion_time: float = 0 # [s]
    try:
        while True:

            # Read the motion sensor
            if sensor.read_motion_sensor() is True: 
                last_motion_time: float = time.time()
                start_music = True

            if music_playing:
                # Check if music should be stopped
                motionless_time: float = time.time() - last_motion_time
                play_time: float = time.time() - start_time

                if motionless_time > p.MIN_MOTIONLESS_TIME and play_time > p.MIN_PLAY_TIME:
                    music.stop()
            else:
                daytime: bool = p.EARLIEST_SOUND <= time.localtime().tm_hour < p.LATEST_SOUND
                if start_music and daytime:
                    music.play(music.load())
                    start_music = False

            time.sleep(p.PERIOD) #Short delay

    except KeyboardInterrupt:
        if p.VERBOSE: print("Exiting program")
    finally:
        sensor.finalize()
        music.finalize()

if __name__ == "__main__":
    initialize()
    main_loop()
