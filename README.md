# MCNode

A Python API for running and extending a Minecraft server.

# Examples

## Make and Extend a Server
This downloads the Minecraft server jar, and starts up a server with the specified options.
GreetBot will also greet people by name when they log in.

```python
from mcnode import MCNode
from greet_bot import GreetBot

node = MCNode({ 
    	'server_jar_url' : 'https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar',
		'server_directory' : './server/',
		'server_jar_path' : 'minecraft_server.jar',
		'init_memory' : '512M',
		'max_memory' : '1024M'
})

node.add_bot(GreetBot(node))
node.read()
```

```python
from mcbot import MCBot

class GreetBot(MCBot):
	def on_connect(self, data):
		self.node.say('Welcome, %s' % (data[3]))
```

# The Full API

## Communicating with the Server

### `node.tell(message)` passes an arbitrary string into the server
Functions like `node.say()`, `node.ban()` and `node.tp()` all extend `node.tell()`.

### `node.say(message)` wrapper for Minecraft's say function
```python
def say(self, message):
	return self.tell('say ' + message)
```

## Killing the Server

### `node.stop()` asks the server to stop
```python
def stop(self):
    return self.tell('stop')
```

### `node.terminate()`
Uses `SIGTERM` (or Windows equivalent). Usually won't cause data loss, but `node.stop()` is still advised.

### `nodekill()` violently destroys the server
Uses `SIGKILL` (or Windows equivalent). This is not advised as it can cause data loss.
