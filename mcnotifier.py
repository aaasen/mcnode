# @aaaasen (Lane Aasen)
# November 2012
# Python 2.7
# Tested on (Arch) Linux

# mcnotifier
# notifies mcnode-compatible servers of updates to the mcnode
# this can be used to easily create web apps for minecraft servers

import requests

class MCNotifier:

	def post(self, data=None):
		return requests.post(self.url, data)

	def __init__(self, url):
		self.url = url

mcnotifier = MCNotifier('http://localhost:3000/players')

player = { 'player[username]' : 'pyplayer', 'player[online]' : 'true', 'player[last_login]' : 'now' }

print mcnotifier.post(player)