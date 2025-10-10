# Ambianceur
Raspberry Pi based ambient sound player. Under developpement.


# Goal
I want to make a prototype device that performs the following function :
- When a movement is detected, a music is started. It plays as long as some activity is detected, but at least for 5 minutes.
- At night (between 22:00 and 7:00), no music is played.
- I want to easily be able to change the music (uploading a new file, inserting a usb stick, ...).
- The device is always plugged in and uses wifi to sync its clock (hour minute seconds)


# RPi setup
1. Flash OS, setup Wifi etc
1. Clone git repo in _/home/pi/Documents_
1. Install requirements : `sudo apt install python3-mypackage` for each package
1. Copy music file(s) in _/home/pi/Music_
1. Autorun python script at boot using _systemd_:
    1. Create a service file: `sudo nano /lib/systemd/system/ambianceur.service`
    1. Enter the following in the file:
    ```plain
    [Unit]
    Description=Python ambianceur service
    After=multi-user.target

    [Service]
    Type=idle
    ExecStart=python /home/pi/Documents/Ambianceur/main.py

    [Install]
    WantedBy=multi-user.target
    ```
    1. Save and exit nano: `ctrl + X`
    1. Make the file executable: `sudo chmod 644 /lib/systemd/system/ambianceur.service`
    1. Enable the service so it starts at boot: `sudo systemctl enable ambianceur.service`