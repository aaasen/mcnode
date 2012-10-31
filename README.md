# MCNode

A Python API to running and extending a Minecraft server.

## Using the API

### create a server
> `node = MCNode({ 
		'server_jar_url' : 'https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar',
		'server_directory' : './server/',
		'server_jar_path' : 'minecraft_server.jar',
		'init_memory' : '512M',
		'max_memory' : '1024M'
})`

This will fetch the Minecraft server jar and start it up with the specified options.

### run a command on the server

> `node.tell('stop')`

`node.tell(str)` passes an arbitrary string into the server.
Functions like `node.say()`, `node.ban()` and `node.tp()` all extend `node.tell()`.
