\# MCNode

A Python API to running and extending a Minecraft server.

## Using the API

### Create a Server
> `node = MCNode({ 
		'server_jar_url' : 'https://s3.amazonaws.com/MinecraftDownload/launcher/minecraft_server.jar',
		'server_directory' : './server/',
		'server_jar_path' : 'minecraft_server.jar',
		'init_memory' : '512M',
		'max_memory' : '1024M'
})`

This will fetch the Minecraft server jar and start it up with the specified options.

### Run a Command on the Server

> `node.tell('stop')`

`node.tell(str)` passes an arbitrary string into the server.
Functions like `node.say()`, `node.ban()` and `node.tp()` all extend `node.tell()`.

### All MCNode Functions (may or may not be implemented)

<table>
  <tr>
    <th>function</th><th>args</th><th>description</th><th>implemented?</th>
  </tr>
  <tr>
    <td>tell</td><td>string</td><td>passes an arbitrary string into the server</td><td>yes</td>
  </tr>
  <tr>
    <td>stop</td><td>goodbye_message</td><td>says goodbye stops the server gently</td><td>yes</td>
  </tr>
  <tr>
    <td>kill</td><td></td><td>violently stops the server (danger!)</td><td>yes</td>
  </tr>
  <tr>
    <td>render</td><td>file_path</td><td>makes a render of the world</td><td>no</td>
  </tr>
  <tr>
    <td>ban</td><td>username</td><td>permabans username</td>
  </tr><td>no</td>
  <tr>
    <td></td><td></td><td></td>
  </tr><td>no</td>
  <tr>
    <td></td><td></td><td></td>
  </tr><td>no</td>
  <tr>
    <td></td><td></td><td></td>
  </tr><td>no</td>
</table>
