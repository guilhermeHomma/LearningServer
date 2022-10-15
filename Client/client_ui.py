from re import S
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')


class Chat:
    def __init__(self, layout, name):
        self.layout = layout
        self.janela = sg.Window(name, layout)
        self.run()

    def showChat(self):
        layout = [
                [sg.Input(key='mensagem')],
                [sg.Button('Enviar')],
        ]
        self.janela = sg.Window('tela chat', layout)
        pass
    
    def run(self):
        while True:
            eventos, valores = self.janela.read()
            if eventos == sg.WINDOW_CLOSED:
                print('break')
                break
            if eventos == 'cadastrar':
                print('Bem-vindo a minha primeira interface!')
                self.name = valores['nome']
                self.showChat()


mylayout = [
        [sg.Text('Nome: '),sg.Input(key='nome')],
        [sg.Button('cadastrar')]
]
chat = Chat(mylayout,'nome')