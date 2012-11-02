
from mcnode import MCNode
from greet_bot import GreetBot

node = MCNode({ 
		'server_jar_url' : 'https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar',
		'server_directory' : './dev_server/',
		'server_jar_path' : 'minecraft_server.jar',
		'init_memory' : '512M',
		'max_memory' : '1024M'
})

node.add_bot(GreetBot(node))

node.read()
