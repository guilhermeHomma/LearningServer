import errno
from http import client
from pickletools import read_uint1
from re import M
from ssl import SOCK_STREAM
import threading
import socket
import os

from client_ui import Chat

class ServerCliente:
    def __init__(self,chat: Chat) -> None:
        self.chat = chat
        self.client = socket.socket(socket.AF_INET,SOCK_STREAM)

        try:
            self.client.connect(('localhost',7777))
        except:
            self.chat.stop()
            return print("não foi possivel conectar")
        
        username = 'user'
        print('\nConectado')

    def StopSocket(self):
        print('STOP OS')
        os.abort()

    def ReceiveMessages(self):
        try:
            msg = self.client.recv(2048).decode('utf-8')
            if type(msg) is str and msg != "":
                self.chat.ReceiveMessage(msg)
        except NameError as error:
            print(error)
            pass

    def sendMessages(self, msg):
        print('client sending...')
        try:
            if msg == '':
                print('message null')
                return
            self.client.send(f'{msg}'.encode('utf-8'))
        except NameError as error: 
            print(error)
            pass

        print('message sent')
