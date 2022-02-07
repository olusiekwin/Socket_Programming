import socket

HEADER = 65
PORT = 5050
FORMAT = 'UTF-8'
DISCONECT_MESSAGE = "!DISCONECT"
SERVER = "192.186.1.__"
ADDR = (SERVER, PORT)

client  = socket.socket(socket.AF_INET, socket.SOCK_SREAM)
client.connect(address)


