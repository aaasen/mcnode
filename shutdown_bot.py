
from mcbot import MCBot

class ShutdownBot(MCBot):
	"""a bot that shuts down the server when someone disconnects"""

	def on_disconnect(self, data):
		self.node.stop()
