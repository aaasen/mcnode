
from mcbot import MCBot

class GreetBot(MCBot):
	"""a bot that says hello to people when they log in"""

	def on_connect(self, data):
		self.node.say('hello')