# @aaaasen (Lane Aasen)
# November 2012
# Python 2.7

# mcnode.py
# outward facing API for mcnode

import urllib
import subprocess
import os

# configuration that may later be put into a file
# dictionaries are awesome for this!!!
config = { 
	'server_jar_url' : 'https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar',
	'server_directory' : './server/',
	'server_jar_path' : 'minecraft_server.jar',
	'init_memory' : '512M',
	'max_memory' : '1024M'
}

# logs an arbitrary message to something
# just wraps print for development, but may log to a file in production
def __log(message):
	print message

# downloads src into dest
def __get_remote_file(src, dest):
	try:
		urllib.urlretrieve(src, dest)
	except IOError:
		__log('__get_remote_file failed to retrieve ' + src)

# updates minecraft_sserver.jar with a fresh version from Minecraft's CDN
def update_server(src=config['server_jar_url'], dest_dir=config['server_directory'], dest=config['server_jar_path']):
	if not os.path.exists(dest_dir):
		os.makedirs(dest_dir)

	__get_remote_file(src, dest_dir + dest)

# returns true if the os supports java from the command line
# TODO: make quiet
def __check_path():
	try:
		subprocess.call('java', stdout=None)
		return True
	except OSError:
		__log('$PATH not set up properly.')
	return False

# spins up the server
def start_server(server_directory=config['server_directory'], init_memory=config['init_memory'], max_memory=config['max_memory'], server_jar_path=config['server_jar_path']):
	# if not __check_path():
	# 	return

	os.chdir(server_directory)
	subprocess.call(['java', '-Xms' + init_memory, '-Xmx' + max_memory, '-jar', server_jar_path, 'nogui'])



update_server()
start_server()
