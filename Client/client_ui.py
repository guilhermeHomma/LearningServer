from re import S
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')


class Chat:
    def __init__(self):
        self.RUNNING : bool = True
        self.username = ''
        self.messages = ['']
        self.lastmessage = ''
        self.window = self.ChatWindow()
        pass

    def stop(self):
        self.RUNNING = False

    def ReceiveMessage(self, message: str):
        self.messages.append(message)

        full_text : str = ''

        for message in self.messages:
            full_text += message+'\n'

        self.window['TEXTBOX'].update(value=full_text)

    def getmessage(self) -> str:
        message = self.lastmessage
        self.lastmessag = ''
        return message

    def ChatWindow(self):
        layout = [
            [sg.Text('', key='TEXTBOX')],
            [sg.Input(key='MESSAGE')],
            [sg.Button('send')]
        ]
        return sg.Window('chat', layout)
        #self.janela = sg.Window('chat', layout)
    
    def update(self):
        events, values = self.window.read()
        if events == sg.WINDOW_CLOSED:
            print("CHAT -> QUIT")
            self.RUNNING = False

        if events == 'send' and values['MESSAGE'] != '':
            self.ReceiveMessage(values['MESSAGE'])
            return values['MESSAGE']

