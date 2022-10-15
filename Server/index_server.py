from http import client
from os import access
import threading
import socket

clients = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost',7777))
        server.listen()
    except:
        return print('\nNão foi possivel iniciar o servidor!')

    while True:
        client, addr = server.accept()
        clients.append(client)

        thread = threading.Thread(target=messageTreatment, args=[client])
        thread.start()


def messageTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break

def broadcast(msg, client):
    for element in clients:
        if element != client:
            try:
                element.send(msg)
            except:
                deleteClient(element)
                pass

def deleteClient(client):
    if client in clients:
        clients.remove(client)

main()