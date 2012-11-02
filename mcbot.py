# @aaaasen (Lane Aasen)
# November 2012
# Python 2.7
# Tested on (Arch) Linux

# mcbot.py
# bots that repsond to events fired by mcnodes
# for example, a mcbot could listen to connect events and welcome users when they log in

class MCBot:
	"""bots that repsond to events fired by mcnodes"""

	def on_connect(self, data):
		return

	def on_disconnect(self, data):
		return

	def on_say(self, data):
		return

	def __init__(self):
		return

bot = MCBot()
