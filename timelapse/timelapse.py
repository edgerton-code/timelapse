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

import argparse
import re

# Initial test of argument handling

time_regex = "^(?:(?:(\d{1,2}):)?(\d{1,2}):)?(\d{1,2})$"
seconds_regex = "^(\d+)$"

class IntervalAction(argparse.Action):
	
	def __call__(self, parser, namespace, values, option_string=None):
		
		print('%r %r %r' % (namespace, values, option_string))
		interval_seconds = 0
		# test for the two possible imputs, seconds or hh:mm:ss
		time_match = re.match(time_regex, values)
		if time_match is not None:
			# it's hh:mm:ss
			# make sure mm and ss is in the range 0..59 unless ss is the only value
			print("interval is hh:mm:ss")
			if time_match.group(1) is None and time_match.group(2) is None:
				# only seconds, allow 1 to 99
				interval_seconds = int(time_match.group(3))
				setattr(namespace, self.dest, values)
				setattr(namespace, 'interval_seconds', interval_seconds)
			else:
				
				# mm:ss both must be 1..60
				tm_hour = 0
				tm_minutes = int(time_match.group(2))
				tm_seconds = int(time_match.group(3))
				if tm_minutes > 59:
					raise argparse.ArgumentError(
						argument=self,
						message="{0} minutes must be less than 60".format(values))
				if tm_seconds > 59:
					raise argparse.ArgumentError(
						argument=self,
						message="{0} seconds must be less than 60 unless only seconds is specified".format(values))
				if time_match.group(1) is not None:
					# fold in hour value
					tm_hour = int(time_match.group(1))
				# calculate interval in seconds
				interval_seconds = (((tm_hour * 60) + tm_minutes) * 60) + tm_seconds
		else:
			seconds_match = re.match(seconds_regex, values)
			if seconds_match is None:
				#parser.error("{0} must be either [[hh:]mm:]ss or seconds".format(values))
				raise argparse.ArgumentError(
					argument=self,
					message="{0} must be either [[hh:]mm:]ss or seconds".format(values))
			print("Large seconds")
			interval_seconds = int(values)
		setattr(namespace, self.dest, values)
		setattr(namespace, 'interval_seconds', interval_seconds)
		

parser = argparse.ArgumentParser(
	description="""
Camera control program for creating time lapse photos.
	""",
	epilog="""The number of photos to take will be the frames per second"""+
	""" times the duration in seconds."""+
	""" For example: 24 FPS for 20 seconds will take 240 photos."""
)

parser.add_argument(
	'--fps',
	default=24,
	type=int,
	help="frames per second (default: %(default)s)")
parser.add_argument(
	'interval',
	action=IntervalAction,
	help="time between photos in [[hh:]mm:]ss")
	
parser.add_argument(
	'duration',
	nargs='?',
	default=20,
	type=int,
	help="time for movie to run in seconds (default: %(default)s)")
	
print(parser.parse_args())

