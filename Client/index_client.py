from http import client
from ssl import SOCK_STREAM
import threading
import socket

def main():
    client = socket.socket(socket.AF_INET,SOCK_STREAM)

    try:
        client.connect(('localhost',7777))
    except:
        return print("não foi possivel conectar")
    
    username = input('Usuário> ')
    print('\nConectado')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()

def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print("\n"+msg)
        except:
            print("\nnão foi possivel manter conexão")
            print("\nPressione <enter> para continuar")
            client.close()
            break
    pass

def sendMessages(client, username):
    while True:
        try:
            msg = input('\n<voce>')
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return
    pass

main()