import argparse
import re

# timelapse argument handling

class TimelapseArgs(object):


	# subclass to handle parsing and validating interval values
	
	class _HelpAction(argparse._HelpAction):
			
		def __call__(self, parser, namespace, values, option_string=None):
			parser.print_help()
			print()
				
			# retrieve subparsers from parser
			subparsers_actions = [
				action for action in parser._actions
				if isinstance(action, argparse._SubParsersAction)]
			# the will probably only be one subparser_action,
			# but better safe than sorry
			for subparsers_action in subparsers_actions:
				# get all subparsers and print help
				for choice, subparser in subparsers_action.choices.items():
					print("Subcommand: {}".format(choice))
					print(subparser.format_help())
				
			parser.exit()



	class IntervalAction(argparse.Action):
		
		time_regex = "^(?:(?:(\d{1,2}):)?(\d{1,2}):)?(\d{1,2})$"
		seconds_regex = "^(\d+)$"
	
		def __call__(self, parser, namespace, values, option_string=None):
		
			print('%r %r %r' % (namespace, values, option_string))
			interval_seconds = 0
			# test for the two possible imputs, seconds or hh:mm:ss
			time_match = re.match(self.time_regex, values)
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
				seconds_match = re.match(self.seconds_regex, values)
				if seconds_match is None:
					raise argparse.ArgumentError(
						argument=self,
						message="{0} must be either [[hh:]mm:]ss or seconds".format(values))
				print("Large seconds")
				interval_seconds = int(values)
			# set the results
			setattr(namespace, self.dest, values)
			setattr(namespace, 'interval_seconds', interval_seconds)
		
	def __init__(self):
		
		self.check_camera = False
		self.shoot = False
	
		self.parser = argparse.ArgumentParser(
			description = "Camera control program for creating time lapse photos.",
			epilog= "The number of photos to take will be the frames per second"+
					" times the duration in seconds."+
					" For example: 24 FPS for 20 seconds will take 240 photos.",
			add_help = False
		)
		
		self.parser.add_argument('--help', action=self._HelpAction, help="help for help")

		subparsers = self.parser.add_subparsers()
		parser_shoot = subparsers.add_parser('shoot',
			help="Start shooting sequence.  Use %(prog)s shoot --help to see valid arguments.",
			add_help = False)

		parser_shoot.add_argument(
			'--fps',
			default=24,
			type=int,
			help="frames per second (default: %(default)s)")
		parser_shoot.add_argument(
			'interval',
			action=self.IntervalAction,
			help="time between photos in [[hh:]mm:]ss")
		parser_shoot.add_argument(
			'duration',
			nargs='?',
			default=20,	# 20 seconds
			type=int,
			help="time for movie to run in seconds (default: %(default)s)")
		parser_shoot.set_defaults(shoot=True)

		test_camera = subparsers.add_parser('check_camera',
			#action='store_true',
			help="Check the connection to the camera and verify the API commands needed are supported.",
			add_help = False)
		test_camera.set_defaults(check_camera=True)
			
	
	def parse_args(self):
		self.args = self.parser.parse_args(namespace=self)
		#print("FPS = {}".format(self.fps))
		#print("Duration = {}".format(self.duration))
		#print("interval = {}".format(self.interval))
		#print("Interval_seconds = {}".format(self.interval_seconds))
		return self
