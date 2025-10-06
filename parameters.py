'''
Parameter file. All constant parameters are declared here.
'''

MOTION_SENSOR_PIN:  int = 17                # Signal pin of the motion sensor.
MUSIC_FOLDER:       str = "/home/pi/music"  # Path to the music folder
MIN_PLAY_TIME:      int = 300               # [s] Minimum playback time
PERIOD:             float = 0.1             # [s] Main loop period
VERBOSE:            bool = True             # Verbose output