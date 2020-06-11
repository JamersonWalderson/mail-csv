
from PyQt5 import QtWidgets, uic
from threading import Thread
import sys

class Ui(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('gui.ui', self)

        # findchield() = serve para encontrar o modulo do item
        self.importarCSVButton = self.findChild(QtWidgets.QPushButton, 'importarCSVButton')
        self.importarCSVButton.clicked.connect(self.importar_csv)

        self.importarMensagemButton = self.findChild(QtWidgets.QPushButton, 'importarMensagemButton')
        self.importarMensagemButton.clicked.connect(self.importar_mensagem)

        self.enviarButton = self.findChild(QtWidgets.QPushButton, 'enviarButton')
        self.enviarButton.clicked.connect(self.enviar)

       # self.gitHubButton = self.findChild(QtWidgets.QPushButton, 'githubButton')
       # self.gitHubButton.clicked.connect(self.github)

        # Armazena o valor digitado no QLineEdit na variavel assunto_da_pesquisa
        self.emailText = self.findChild(QtWidgets.QLineEdit, 'emailText')
        self.senhaSenha = self.findChild(QtWidgets.QLineEdit, 'senhaText')

        self.show()

    def importar_csv(self):
        print ("Importar CSV")
    
    def importar_mensagem(self):
        print ("Importar Mensagem")

    def enviar(self):
        print ("Enviar")

    def github(self):
        print ("Github")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()