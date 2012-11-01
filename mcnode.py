# @aaaasen (Lane Aasen)
# November 2012
# Python 2.7

# mcnode.py
# outward facing API for mcnode

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
	"""A Minecraft server."""

	parse_helpers = {
		'username' : '([a-zA-Z0-9]{3,20})',
		'ip' : '\[/([0-9\.])',
		'line_start' : 'asd'
	}

	#  % (parse_helpers['username'], parse_helpers['ip'])
	parsers = {
		'connect' :  'logged in',
		'disconnect' : 'lost connection',
		'say' : '<(%s)>([^\n\r]*)' % (parse_helpers['username'])
	}

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

	# returns the status of the server process as a subprocess 'returncode'
	def poll(self):
		return self.server_process.isalive()

	# sends an arbitrary string to the node's stdin
	def tell(self, message):
		return self.server_process.sendline(message)

	def read(self):
		while True:
			index = self.server_process.expect(self.parsers.values())
			print self.parsers.keys()[index]
			print self.server_process.match.group(0)
			print self.server_process.match.groups()

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
		self.update_server()
		self.start_server()

node = MCNode({ 
		'server_jar_url' : 'https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar',
		'server_directory' : './dev_server/',
		'server_jar_path' : 'minecraft_server.jar',
		'init_memory' : '512M',
		'max_memory' : '1024M'
})

node.read()

