from concurrent.futures import thread
from client_ui import Chat
from index_client import ServerCliente
from index_client import *
import threading
import time
import socket

name = input('name: ')
chat : Chat = Chat(name)
server = ServerCliente(chat)

def main():
    thread_server = threading.Thread(target=server_run)
    thread_server.start()
    chat_run(name)

def chat_run(name):
    while chat.RUNNING:
        time.sleep(0.1)
        msg = chat.SendMessage()
        if msg != "":
            threading.Thread(target=send_message, args=[msg, name]).start()
        chat.update()

    chat.RUNNING = False
    server.StopSocket()
    print('USER CHAT -> QUIT')

def send_message(msg , name):
    server.sendMessages(f'{name}: {msg}')

def server_run():
    print('waiting for messages')
    while chat.RUNNING:
        server.ReceiveMessages()

    print('USER SERVER -> QUIT')

main()