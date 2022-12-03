import utils._socket as us
server = us.Server(5528, '192.168.31.164')
print(server.info())
server.open()