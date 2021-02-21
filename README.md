# Timelapse

Timelapse is a command line program for shooting photos to be used to
 create a timelapse movie.

I chose to use a command line interface instead of a graphical interface
such as petabite's PyLapse so I could run it on
a Raspberry Pi 3b headless using ssh into the computer.  It works with
 the Sony wifi interface between the camera and the
Raspberry Pi and the unit is small enough to be mounted on the tripod
 with the camera.

I'm using a Sony DSC HX-80, mounted on a lightweight tripod.  Due to the
small size of the Raspberry's WIFI antenna, it needs to be close to have
a strong signal that prevents connection dropouts during the shooting
sequence.

## Installation

This program depends on petabite's libsonyapi python binding for the
Sony Camera API.

Currently using python 3.7.3

## Usage
```
python timelapse.py --help
usage: timelapse.py [--help] {shoot,check_camera} ...

Camera control program for creating time lapse photos.

positional arguments:
  {shoot,check_camera}
    shoot               Start shooting sequence. Use timelapse.py shoot --help
                        to see valid arguments.
    check_camera        Check the connection to the camera and verify the API
                        commands needed are supported.

optional arguments:
  --help                help for help

The number of photos to take will be the frames per second times the duration
in seconds. For example: 24 FPS for 20 seconds will take 240 photos.

Subcommand: shoot
usage: timelapse.py shoot [--fps FPS] interval [duration]

positional arguments:
  interval   time between photos in [[hh:]mm:]ss
  duration   time for movie to run in seconds (default: 20)

optional arguments:
  --fps FPS  frames per second (default: 24)

Subcommand: check_camera
usage: timelapse.py check_camera

```
## Notes

On the Raspberry Pi I added a USB WIFI dongle.  this gives:
```
	wlan0	camera
	wlan1	my router for ssh in
```

If the connections are reversed the camera module could not discover the camera.  Might have to add an option to indicate which wlan is connected to the camera.

## Dependencies

```
Python 3.7.3 on Raspberry Pi is what I am currently using

	petabite/libsonyapi		wrapper for the Sony camera API
	netifaces				pip install netifaces - to determine the connected ethernet interfaces
	
On the camera:

	Smart Remote Control	Playmemories Camera App - sadly it only supports a WIFI connection.
```
	
