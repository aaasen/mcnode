# @aaaasen (Lane Aasen)
# November 2012
# Python 2.7

# mcnode.py
# outward facing API for mcnode

import urllib
import subprocess
import os
import time

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
		self.server_process = subprocess.Popen(['java', '-Xms' + self.config['init_memory'], '-Xmx' + self.config['max_memory'], '-jar', self.config['server_jar_path'], 'nogui'], stdin=subprocess.PIPE)

	def poll(self):
		return self.server_process.poll()

	def help(self):
		print self.server_process.communicate('help')

	def kill(self):
		self.server_process.kill()

	def __init__(self, config):
		self.config = config
		self.start_server()

node = MCNode({ 
		'server_jar_url' : 'https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar',
		'server_directory' : './server/',
		'server_jar_path' : 'minecraft_server.jar',
		'init_memory' : '512M',
		'max_memory' : '1024M'
})

node.help()
node.kill()
