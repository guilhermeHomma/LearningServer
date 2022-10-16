from http import client
from ssl import SOCK_STREAM
import threading
import socket

from client_ui import Chat

class ServerCliente:
    def __init__(self,chat: Chat) -> None:
        self.chat = chat
        pass

    def StartServer(self):
        self.client = socket.socket(socket.AF_INET,SOCK_STREAM)
        try:
            self.client.connect(('localhost',7777))
        except:
            self.chat.stop()
            return print("não foi possivel conectar")
        
        username = 'user'

        print('\nConectado')

        self.thread1 = threading.Thread(target=self.receiveMessages)
        self.thread2 = threading.Thread(target=self.sendMessages)

        self.thread1.start()
        self.thread2.start()

    def receiveMessages(self):
        print('receiving')
        while self.chat.RUNNING:
            msg = self.client.recv(2048).decode('utf-8')
            try:
                if self.chat.RUNNING:
                    self.chat.ReceiveMessage(msg)
                else:
                    return
            except:
                print("SERVER -> Desconectado")
                self.chat.stop()
                self.client.close()
                break
        print('thread receive -> FINISH')

    def sendMessages(self):
        while self.chat.RUNNING:
            try:
                msg = self.chat.getmessage()
                if msg == '':
                    continue
                self.client.send(f'{msg}'.encode('utf-8'))
            except:
                return
        print('thread send -> FINISH')
