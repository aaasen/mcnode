# MCNode

A Python API for running and extending a Minecraft server.

# Quick Start

## Create a Server
```python
node = MCNode({
		'server_jar_url' : 'https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar',
		'server_directory' : './server/',
		'server_jar_path' : 'minecraft_server.jar',
		'init_memory' : '512M',
		'max_memory' : '1024M'
>})
```

This will fetch the Minecraft server jar and start it up with the specified options.

## Run a Command on the Server

```python
node.tell('stop')
```

`node.tell(str)` passes an arbitrary string into the server.
Functions like `node.say()`, `node.ban()` and `node.tp()` all extend `node.tell()`.

# Complete MCNode API

## killing functions

### `stop()` asks the server to stop
```python
def stop(self):
    return self.tell('stop')
```

### `terminate()`
Uses `SIGTERM` (or Windows equivalent). Usually won't cause data loss, but `stop()` is still advised.

### `kill()` violently destroys the server
Uses `SIGKILL` (or Windows equivalent). This is not advised as it can cause data loss.

