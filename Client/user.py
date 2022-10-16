from client_ui import Chat
from index_client import ServerCliente
from index_client import *

def main():
    mychat = Chat()
    myserver = ServerCliente(mychat)
    
    myserver.StartServer()

    thread = threading.Thread(target=chatrun, args=[mychat])
    thread.start()


def chatrun(chat : Chat):
    while chat.RUNNING:
        chat.update()

main()