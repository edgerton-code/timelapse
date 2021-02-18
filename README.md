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

python timelapse.py [-h] [--fps FPS] interval [duration]

Camera control program for creating time lapse photos.

positional arguments:
  interval    time between photos in [[hh:]mm:]ss
  duration    time for movie to run in seconds (default: 20)

optional arguments:
  -h, --help  show this help message and exit
  --fps FPS   frames per second (default: 24)

The number of photos to take will be the frames per second times the duration
in seconds. For example: 24 FPS for 20 seconds will take 240 photos.
