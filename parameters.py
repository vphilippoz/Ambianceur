'''
Parameter file. All constant parameters are declared here.
'''

MOTION_SENSOR_PIN:  int = 18                # Signal pin of the motion sensor (BOARD).
MUSIC_FOLDER:       str = "/home/pi/music"  # Path to the music folder
MIN_PLAY_TIME:      int = 300               # [s] Minimum playback time
MIN_MOTIONLESS_TIME:int = 30                # [s] Time without motion to stop music
EARLIEST_SOUND:     float = 7.0             # [h] Earliest hour to play sound
LATEST_SOUND:       float = 23.0            # [h] Latest hour to play sound
FADEOUT_TIME:       int = 1000              # [ms] Time to fade out the music
PERIOD:             float = 0.2             # [s] Main loop period
VERBOSE:            bool = True             # Verbose output