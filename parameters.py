'''
Parameter file. All constant parameters are declared here.
'''

MOTION_SENSOR_PIN:  int = 17                # Signal pin of the motion sensor.
MUSIC_FOLDER:       str = "/home/pi/music"  # Path to the music folder
MIN_PLAY_TIME:      int = 300               # [s] Minimum playback time
MIN_MOTIONLESS_TIME:int = 30                # [s] Time without motion to stop music
PERIOD:             float = 0.2             # [s] Main loop period
VERBOSE:            bool = True             # Verbose output