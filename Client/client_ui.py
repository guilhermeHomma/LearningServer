from re import S
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')


class Chat:
    def __init__(self, name):
        self.RUNNING : bool = True
        self.username = name
        self.messages = [ '' , '' , '' , '' , '' ]
        self.lastmessage = ''
        self.window = self.ChatWindow()
        pass

    def stop(self):
        self.RUNNING = False
        self.window.close()

    def ReceiveMessage(self, message: str):
        self.messages.append(message)
        self.messages.pop(0)

        full_text : str = ''

        for message in self.messages:
            full_text += message+'\n'

        self.window['TEXTBOX'].update(value=full_text)

    def SendMessage(self) -> str:
        message = self.lastmessage
        print(message)
        self.lastmessage = ''
        return message

    def ChatWindow(self):
        layout = [
            [sg.Text('\n \n \n \n \n', key='TEXTBOX')],
            [sg.Input(key='MESSAGE',do_not_clear=False)],
            [sg.Button('send')]
        ]
        return sg.Window(self.username +' chat', layout)
        #self.janela = sg.Window('chat', layout)
    
    def update(self):
        events, values = self.window.read()
        if events == sg.WINDOW_CLOSED:
            print("CHAT -> QUIT")
            self.RUNNING = False

        if events == 'send' and values['MESSAGE'] != '':
            self.lastmessage = values['MESSAGE']
            self.ReceiveMessage(f'you: '+values['MESSAGE'])

