# Ambianceur
Raspberry Pi based automated audio player. Use it in any room where you want to create an ambiance! 

I use this device plays ambiant sounds, such as forest, rain or wind recordings. The audio is started as soon as movement is detected, and ends 30 seconds after the movement stops. Also, the device remain silent at night.

# Required material
- Raspberry Pi 3B+ or newer, with an adapted power supply
- PIR sensor (for example, [BS412](https://www.adafruit.com/product/4666))
- Speaker with integrated amplifier (for example, [Adafruit STEMMA Speaker](https://www.adafruit.com/product/4666))
- A few cables, solder and a soldering iron
- Header socket (2.54 mm pitch) to connect peripherals to the Raspberry Pi. Alternatively, wires can be soldered directly to the board headers, but I would not recommand it.
    - 1x 01x01 pin configuration
    - 2x 01x02 pins configuration
- An old jack 3.5 mm cable that you are willing to destroy
- A 3D printer 
- 3D printing filament (~100g is necessary, depending on your slicing parameters)
- 3x M3 heat set threaded inserts
- 3x M3x5 socket head cap screws
- 8x M2.5x6 socket head cap screws
- Audio files you want to play in _.mp3_ format

# Instructions

## Setup the Raspberry Pi
1. Flash OS, setup Wifi, user and password (_pi_, _pipipipi_), etc.
1. Clone git repo in _/home/pi/Documents_
1. Install requirements : `sudo apt install python3-mypackage` for each package
1. Copy desired audio file(s) in _/home/pi/Music_
2. Disable the HDMI audio so the Jack 3.5 is used by default:
    1. Edit the configuration file: `sudo nano /boot/config.txt`
    2. Add the following:
       ```
       hdmi_ignore_edid_audio=1
       audio_pwm_mode=2
       ```
    4. Save and exit using _ctrl + X_
1. Autorun python script at boot using a _.desktop_ file (other methods such as _systemd_ do not work as the desktop env is required to play sound):
    1. Create the autostart directory: `mkdir -p /home/pi/.config/autostart`
    2. Create the file: `sudo nano /home/pi/.config/autostart/ambianceur.desktop`
    3. Enter the following in the file:
        ```
        [Desktop Entry]
        Type=Application
        Exec=python /home/pi/Documents/Ambianceur/main.py
        ```
    5. Save and exit using _ctrl + X_

## Printing the case
Any 3D printer can be used to print the case. I used an Ender 3 V3 with PETG filament.

1. Download the 3D files in _.stl_ format located in _Ambianceur/3D/_
1. Open your slicing software and import the files
1. Slice the file using your prefered parameters. I used 0.2 mm layer height and 2 wall perimeters.
1. Start printing!

## Soldering the electronics
Connect as follow:

**PIR:** 
- GND (VSS) and ONTIME -> 01x01 header socket. Will connect to pin 20 of Raspberry Pi (GND)
- VDD -> one pin of 01x02 header socket #1. Will connect to pin 17 of Raspberry Pi (3.3V)
- REL -> other pin of 1x02 header socket #1. Will connect to pin 18 of Raspberry Pi (GPIO 24)

**Audio amplifier:**
- +5V -> one pin of 01x02 header socket #2. Will connect to pin 4 of Raspberry Pi (5V)
- GND -> other pin of 01x02 header socket #2. Will connect to pin 6 of Raspberry Pi (GND)
- Jack 3.5mm GND -> GND pad on audio amplifier
- Jack 3.5mm Signal -> Signal pad on audio amplifier

## Assembly
1. Insert PIR sensor in the intended hole. If it is loose, use some glue, tape or similar to keep it in place.
1. Screw the audio amplifier board using four M2.5x6 screws.
1. Wire everything as explained in the previous section
1. Screw the Raspberry Pi using the remaining M2.5x6 screws.
1. Plug the power supply to the Raspberry Pi through the intended hole.
1. Screw the cover using three M3x5 screws

## Testing
Plug the power supply into a wall outlet. After less than 5 minutes, the device should be operationnal. Have fun!
