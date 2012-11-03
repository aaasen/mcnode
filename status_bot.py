# @aaaasen (Lane Aasen)
# November 2012
# Python 2.7
# Tested on (Arch) Linux

# status_bot.py
# notifies an external server of all events

from mcbot import MCBot
from mcnotifier import MCNotifier

class StatusBot(MCBot):
	"""a bot that says hello to people when they log in"""

	def on_connect(self, data):
		self.mcnotifier.post({ 'player[username]' : data[3], 'player[online]' : 'true' })

	def __init__(self, node, url):
		self.node = node
		self.mcnotifier = MCNotifier(url)
