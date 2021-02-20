#
#
# timelapse - derived from Pylapse, pure command line interface
#
# Usage:
#
#    timelapse --fps=# --interval=time --duration=time
#
#    time is [mm:]ss
#
#	 fps default to 24 frames per second

import tlargs
from libsonyapi.camera import Camera
from libsonyapi.actions import Actions

# Initial test of argument handling

tl_arg_parser = tlargs.TimelapseArgs()
tl_args = tl_arg_parser.parse_args()
print(vars(tl_args))


if tl_args.check_camera:
	print("Got check_camera")
	camera = Camera()  # create camera instance
	camera_info = camera.info()  # get camera camera_info
	print("Camera info: {}".format(camera_info))

	print("Camera name: {}".format(camera.name))  # print name of camera
	print("API version: {}".format(camera.api_version))  # print api version of camera

elif tl_args.shoot:
	print("FPS = {}".format(tl_args.fps))
	print("Duration = {}".format(tl_args.duration))
	print("interval = {}".format(tl_args.interval))
	print("Interval_seconds = {}".format(tl_args.interval_seconds))


