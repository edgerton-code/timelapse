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
import datetime

class Timelapse(object):
	
	def check_camera(self):
		
		print("Check camera connection and abilities")
		try:
			self.camera = Camera()  # create camera instance
			camera_info = self.camera.info()  # get camera camera_info
			print("Camera info: {}".format(camera_info))

			print("Camera name: {}".format(self.camera.name))  # print name of camera
			print("API version: {}".format(self.camera.api_version))  # print api version of camera
		except Exception as ex:
			print("Connection to camera failed.")
			print(ex)
			exit()

	def timelapse_shoot(self):
		self.shots_taken = 0
		while self.shots_taken <= self.total_shots:
			self.camera.do(Actions.actTakePicture)
			time.sleep(interval_in_sec)
			self.shots_taken += 1

	def __init__(self):
		#
		# get command line arguments
		#
		self.check_camera_flag = False
		self.shoot_flag = False
		
		tl_arg_parser = tlargs.TimelapseArgs()
		tl_args = tl_arg_parser.parse_args()
		
		if tl_args.check_camera_flag:
			self.check_camera_flag = True
		if tl_args.shoot_flag:
			# arguments set with shoot sub command
			self.shoot_flag = True
			self.fps = tl_args.fps
			self.duration = tl_args.duration
			self.interval = tl_args.interval
			self.interval_seconds = tl_args.interval_seconds
			self.total_shots = self.duration * self.fps
			self.shoot_duration = self.total_shots * self.interval_seconds


tl = Timelapse();

if tl.check_camera_flag:
	print("Got check_camera")
	tl.check_camera()
	
elif tl.shoot_flag:
	print("FPS = {}".format(tl.fps))
	print("Duration = {} seconds".format(tl.duration))
	print("interval input = {}".format(tl.interval))
	print("Interval_seconds = {} seconds".format(tl.interval_seconds))
	print("Total shots = {}".format(tl.total_shots))
	print("Shoot duration = {}".format(tl.shoot_duration))
	print("Shoot elapsed time = {}".format(str(datetime.timedelta(seconds=tl.shoot_duration))))


