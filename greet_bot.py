# @aaaasen (Lane Aasen)
# November 2012
# Python 2.7
# Tested on (Arch) Linux

# greet_bot.py
# greets users by name when the log in

from mcbot import MCBot

class GreetBot(MCBot):
	"""a bot that says hello to people when they log in"""

	def on_connect(self, data):
		self.node.say('Welcome, %s' % (data[3]))
