# Ambianceur
Raspberry Pi based ambient sound player. 

**Under developpement.**

# Goal
I want to make a prototype device that performs the following function :
- When a movement is detected, a music is started. It plays as long as some activity is detected, but at least for 5 minutes.
- At night (between 23:00 and 6:30), no music is played.
- I want to easily be able to change the music (uploading a new file, inserting a usb stick, ...).
- The device is always plugged in and uses wifi to sync its clock (hour minute seconds)

# Required material
- Raspberry Pi 3B+ or newer
- PIR sensor (for example, [BS412](https://www.adafruit.com/product/4666))
- Speaker with integrated amplifier (for example, [Adafruit STEMMA Speaker](https://www.adafruit.com/product/4666))
- A few cables, solder and a soldering iron
- Header socket (2.54 mm pitch) to connect peripherals to the Raspberry Pi. Alternatively, wires can be soldered directly to the board headers, but I would not recommand it.
    - 1x 01x01 pin configuration
    - 2x 01x02 pins configuration
- A 3D printer 
- 3D printing filament (~100g is necessary, depending on your slicing parameters)
- 3x M3 heat set threaded inserts
- 3x M3x5 socket head cap screws
- 8x M2.5x5 socket head cap screws

# Instructions

## Setup the Raspberry Pi
1. Flash OS, setup Wifi etc
1. Clone git repo in _/home/pi/Documents_
1. Install requirements : `sudo apt install python3-mypackage` for each package
1. Copy music file(s) in _/home/pi/Music_
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

## Soldering the electronics

## Assembly

## Testing
