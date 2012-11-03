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

	def get_url(self, username):
		return self.player_notifier.url + username

	def on_connect(self, data):
		self.player_notifier.post({ 'player[username]' : data[3], 'player[online]' : 'true' })
		self.player_notifier.put({ 'player[username]' : data[3], 'player[online]' : 'true' }, self.get_url(data[3]))

	def on_disconnect(self, data):
		self.player_notifier.put({ 'player[username]' : data[3], 'player[online]' : 'false' }, self.get_url(data[3]))

	def on_say(self, data):
		self.comment_notifier.post({ 'comment[content]' : data[4], 'comment[commenter]' : data[3] })

	def __init__(self, node, url):
		self.node = node
		self.player_notifier = MCNotifier(url + 'players')
		self.comment_notifier = MCNotifier(url + 'comments')
