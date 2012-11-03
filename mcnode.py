# @aaaasen (Lane Aasen)
# November 2012
# Python 2.7
# Tested on (Arch) Linux

# mcnode.py
# python wrapper for minecraft servers

import urllib
import subprocess
import os
import time
import pexpect

# downloads src into dest
def get_remote_file(src, dest):
	try:
		urllib.urlretrieve(src, dest)
	except IOError:
		__log('__get_remote_file failed to retrieve ' + src)

# returns true if the os supports java from the command line
# TODO: make quiet
def check_path():
	try:
		subprocess.call('java', stdout=None)
		return True
	except OSError:
		return False

class MCNode:
	"""a python wrapper for minecraft servers."""

	parse_helpers = {
		'username' : '([a-zA-Z0-9]{3,20})',
		'ip' : '\[/([^\]]*)',
		'date' : '([0-9]{4}-[0-9]{1,2}-[0-9]{1,2})',
		'time' : '([0-9]{2}:[0-9]{2}:[0-9]{2})',
		'log_type' : '\[(INFO|WARNING|ERROR)\]'
	}

	combined_parse_helpers = {
		'line_start' : '%s %s %s' % (parse_helpers['date'], parse_helpers['time'], parse_helpers['log_type'])
	}

	parsers = {
		'connect' : '%s %s%s' % (combined_parse_helpers['line_start'], parse_helpers['username'], parse_helpers['ip']),
		'disconnect' : '%s %s lost connection: ([^\n\r]*)' % (combined_parse_helpers['line_start'], parse_helpers['username']),
		'say' : '%s <%s> ([^\n\r]*)' % (combined_parse_helpers['line_start'], parse_helpers['username'])
	}

	# bots registered with the mcnode
	bots = []

	# logs an arbitrary message to something
	# just wraps print for development, but may log to a file in production
	def __log(message):
		print message

	# updates minecraft_sserver.jar with a fresh version from Minecraft's CDN
	def update_server(self):
		if not os.path.exists(self.config['server_directory']):
			os.makedirs(self.config['server_directory'])

		get_remote_file(self.config['server_jar_url'], self.config['server_directory'] + self.config['server_jar_path'])

	# spins up the server
	def start_server(self):
		# if not __check_path():
		# 	return

		os.chdir(self.config['server_directory'])
		self.server_process = pexpect.spawn('java -Xms%s -Xmx%s -jar %s nogui' % (self.config['init_memory'], self.config['max_memory'], self.config['server_jar_path']))

	# registers a bot with the node so it can respond to events
	def add_bot(self, bot):
		self.bots.append(bot)

	# adds a list of bots
	def add_bots(self, bots):
		for bot in bots:
			self.add_bot(bot)

	# returns the status of the server process as a subprocess 'returncode'
	def poll(self):
		return self.server_process.isalive()

	# sends an arbitrary string to the node's stdin
	def tell(self, message):
		return self.server_process.sendline(message)

	def read(self):
		while True:
			index = self.server_process.expect(self.parsers.values())
			event =  self.parsers.keys()[index]
			data = self.server_process.match.groups()

			print event
			print data

			for bot in self.bots:
				if event == 'connect':
					bot.on_connect(data)
				elif event == 'disconnect':
					bot.on_disconnect(data)
				elif event == 'say':
					bot.on_say(data)
				else:
					print 'unknown event'

	def say(self, message):
		return self.tell('say ' + message)

	# asks the server to stop
	def stop(self):
		return self.tell('stop')

	# gently shuts down the server
	def terminate(self):
		self.server_process.terminate()

	# violently kills the server
	def kill(self):
		self.server_process.terminate(force=True)

	def __init__(self, config):
		self.config = config
		# self.update_server()
		self.start_server()
