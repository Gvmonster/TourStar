import socket as sk
from threading import Thread

def startServer():
    address = ('', 1234)
    connection = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    connection.bind(address)
    connection.listen(4)

    while True:
        userConnection, userAddress = connection.accept()
        threadConnection = Thread(target=handle, daemon=True, args=(userConnection,))


def handle(connection):
    pass
