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

# Initial test of argument handling

tl_arg_parser = tlargs.TimelapseArgs()
tl_args = tl_arg_parser.parse_args()
print(vars(tl_args))


if tl_args.check_camera:
	print("Got check_camera")
elif tl_args.shoot:
	print("FPS = {}".format(tl_args.fps))
	print("Duration = {}".format(tl_args.duration))
	print("interval = {}".format(tl_args.interval))
	print("Interval_seconds = {}".format(tl_args.interval_seconds))


