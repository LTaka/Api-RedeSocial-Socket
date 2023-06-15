from PySide6.QtWidgets import (
    QWidget, 
    QLabel, 
    QLineEdit, 
    QVBoxLayout, 
    QGridLayout, 
    QPushButton, 
    QMessageBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from connect import Connect
from functools import partial

class Enrollment(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cadastro")
        self.setupUI()

    def cadastrarClicked(self):
        #Requisição post
        inputs = [self.nomeInput.text(), 
                  self.emailInput.text(), 
                  self.senhaInput.text(),
                  self.cursoInput.text(),
                  self.universidadeInput.text()]
        for input in inputs:
            if not input:
                QMessageBox.warning(self, "Erro de Cadastro", "Um ou mais campos em branco\nPor favor, entre com todos os dados pedidos")
                return
            
        enrollment_post_request = {'method': 'POST', 
                                    'usage': 'user_register',
                                    'name': self.nomeInput.text(),
                                    'email': self.emailInput.text(),
                                    'password': self.senhaInput.text(),
                                    'course': self.cursoInput.text(),
                                    'university': self.universidadeInput.text()}
        socket=Connect()
        response = socket.typeConnect(enrollment_post_request)
        self.voltarClicked()
            

    def voltarClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.login()

    def setupUI(self):
        self.layout = QVBoxLayout()
        self.gridLayout = QGridLayout()
        # Configuração da interface gráfica...

        self.resize(600, 400)  # Define o tamanho da janela para

        #Botao Voltar
        self.voltarButton = QPushButton("Voltar")
        self.voltarButton.setFixedSize(50, 25)
        self.voltarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        self.voltarButton.clicked.connect(self.voltarClicked)
        self.layout.addWidget(self.voltarButton)
        self.setLayout(self.layout)
    

        # Labels
        self.nomeLabel = QLabel("Nome:")
        self.emailLabel = QLabel("E-mail:")
        self.senhaLabel = QLabel("Senha:")
        self.cursoLabel = QLabel("Curso:")
        self.universidadeLabel = QLabel("Universidade:")

        # Configurando a fonte dos labels
        fonte = QFont("Arial", 12)  # Fonte Arial, tamanho 12
        self.nomeLabel.setFont(fonte)
        self.emailLabel.setFont(fonte)
        self.senhaLabel.setFont(fonte)
        self.cursoLabel.setFont(fonte)
        self.universidadeLabel.setFont(fonte)

        # Campos de input
        self.nomeInput = QLineEdit()
        self.emailInput = QLineEdit()
        self.senhaInput = QLineEdit()
        self.cursoInput = QLineEdit()
        self.universidadeInput = QLineEdit()

        # Logo
        self.logoLabel = QLabel()

        # Carregar a imagem
        self.pixmap = QPixmap("client/images/logo.png")  # Substitua "logo.png" pelo caminho e nome do seu arquivo de imagem

        # Redimensionar a imagem
        width = 200  # Largura desejada
        height = 200  # Altura desejada
        scaledPixmap = self.pixmap.scaled(width, height)

        # Definir a imagem redimensionada como pixmap para o QLabel
        self.logoLabel.setPixmap(scaledPixmap)

        # Botão cadastrar
        self.cadastrarButton = QPushButton("Cadastrar")
        self.cadastrarButton.setFixedSize(100, 45)  # Define o tamanho fixo do botão (200 pixels de largura por 50 pixels de altura)
        self.cadastrarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")  # Define a cor de fundo como azul e a cor do texto como branco
        self.cadastrarButton.clicked.connect(partial(self.cadastrarClicked))
        self.nomeInput.clear()
        self.emailInput.clear()
        self.senhaInput.clear()
        self.cursoInput.clear()
        self.universidadeInput.clear()

        # Configuração do grid layout
        self.gridLayout.addWidget(self.voltarButton, 0, 0, alignment=Qt.AlignLeft)
        self.gridLayout.addWidget(self.nomeLabel, 1, 0)
        self.gridLayout.addWidget(self.emailLabel, 1, 1)
        self.gridLayout.addWidget(self.nomeInput, 2, 0)
        self.gridLayout.addWidget(self.emailInput, 2, 1)
        self.gridLayout.addWidget(self.senhaLabel, 3, 0)
        self.gridLayout.addWidget(self.cursoLabel, 3, 1)
        self.gridLayout.addWidget(self.senhaInput, 4, 0)
        self.gridLayout.addWidget(self.cursoInput, 4, 1)
        self.gridLayout.addWidget(self.universidadeLabel, 5, 1, alignment=Qt.AlignTop)
        self.gridLayout.addWidget(self.universidadeInput, 6, 1, alignment=Qt.AlignTop)
        self.gridLayout.addWidget(self.cadastrarButton, 7, 1, alignment=Qt.AlignCenter)
        self.gridLayout.addWidget(self.logoLabel, 7, 0, alignment=Qt.AlignCenter)  # Posição da logo na grade
    
        # Adiciona os widgets ao layout principal
        self.layout.addLayout(self.gridLayout)
        #layout.addWidget(cadastrarButton)

        self.setLayout(self.layout)