import time
import parameters as p
import music, sensor

def initialize() -> None:
    """
    Set up motion detection and audio playback.
    """
    sensor.initialize()
    music.initialize()

def main_loop() -> None:
    """
    Main program loop.

    Reads the motion sensor and controls music playback based on motion detection and time constraints.
    """
    music_start_time: float = 0 # [s]
    start_music: bool = False
    last_motion_time: float = 0 # [s]
    try:
        while True:
            # Read the motion sensor
            if sensor.read_motion_sensor() == True: 
                last_motion_time: float = time.time()
                start_music = True

            if music.is_playing():
                # Check if music should be stopped
                motionless_time: float = time.time() - last_motion_time
                play_time: float = time.time() - music_start_time

                if motionless_time > p.MIN_MOTIONLESS_TIME and play_time > p.MIN_PLAY_TIME:
                    music.stop()
            else:
                # Check if music should be started
                daytime: bool = p.EARLIEST_SOUND <= time.localtime().tm_hour + time.localtime().tm_min/60.0 < p.LATEST_SOUND
                if start_music and daytime:
                    music_start_time = music.play(music.load())
                    start_music = False

            time.sleep(p.PERIOD)
            start_music = False # Do not memorise detection for next loop

    except KeyboardInterrupt:
        if p.VERBOSE: print("Exiting program")
    finally:
        sensor.finalize()
        music.finalize()

if __name__ == "__main__":
    initialize()
    main_loop()
