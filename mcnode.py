# @aaaasen (Lane Aasen)
# November 2012
# Python 2.7

# mcnode.py
# outward facing API for mcnode

import urllib

# configuration that may later be put into a file
# dictionaries are awesome for this!!!
config = { 
	'server_jar_url' : 'https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar',
	'server_jar_path' : './minecraft_server.jar'
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
def update_server():
	__get_remote_file(config['server_jar_url'], config['server_jar_path'])

update_server()