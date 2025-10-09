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
1. Clone git repo in /home/pi/Documents
1. Install requirements : `sudo apt install python3-mypackage` for each package
1. Autorun python script at boot using systemd:

Type `sudo nano /lib/systemd/system/ambianceur.service`

```plain
Enter the following in the file:
[Unit]
Description=Python ambianceur service
After=multi-user.target

[Service]
Type=idle
ExecStart=python /home/pi/Documents/Ambianceur/main.py

[Install]
WantedBy=multi-user.target
```

Save and exit nano.

Type `sudo chmod 644 /lib/systemd/system/ambianceur.service`