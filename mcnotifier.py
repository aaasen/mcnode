# @aaaasen (Lane Aasen)
# November 2012
# Python 2.7
# Tested on (Arch) Linux

# mcnotifier
# notifies mcnode-compatible servers of updates to the mcnode
# this can be used to easily create web apps for minecraft servers

import requests

requests.max_redirects = 1024

class MCNotifier:

	def post(self, data=None, url=None):
		return requests.post(url if url else self.url, data)

	def put(self, data=None, url=None):
		return requests.put(url if url else self.url, data)

	def __init__(self, url):
		self.url = url + ('' if url[-1] == '/' else '/')
