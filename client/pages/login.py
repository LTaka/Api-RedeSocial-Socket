from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QHBoxLayout,
    QMessageBox
)
from connect import Connect

class LoginPage(QWidget):
    def __init__(self, user_session, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.setupUI(user_session)

    def send_data_to_server(self, user_session):
        email = self.emailInput.text()
        password = self.senhaInput.text()

        post_login = {
            'method': 'POST',
            'usage':'login',
            'email':email,
            'password':password
        }
        socket = Connect()
        response = socket.typeConnect(post_login)

        if(response['status'] != 'ERROR'):
            user_session.set_user_id(response['id_user'])
            self.emailInput.clear()
            self.senhaInput.clear()

            main_window = self.parent().parent()  # Obtenha a instância de MainWindow
            main_window.home()
        else:
            QMessageBox.warning(self, "Erro de login", "E-mail ou senha inválidos.")
            
    def cadastrarClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.cadastro()

    def setupUI(self, user_session):
        self.layout = QHBoxLayout()
        self.gridLayout = QGridLayout()
        # Configuração da interface gráfica...

        self.resize(600, 400)  # Define o tamanho da janela para
    
        # Labels
        self.emailLabel = QLabel("E-mail:")
        self.senhaLabel = QLabel("Senha:")
        self.cadastrarLabel = QLabel("Não possui conta?")

        # Configurando a fonte dos labels
        fonte = QFont("Arial", 12)  # Fonte Arial, tamanho 12
        self.emailLabel.setFont(fonte)
        self.senhaLabel.setFont(fonte)
        self.cadastrarLabel.setFont(fonte)

        # Campos de input
        self.emailInput = QLineEdit()
        self.senhaInput = QLineEdit()
        self.senhaInput.setEchoMode(QLineEdit.Password)

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

        # Botão login
        self.loginButton = QPushButton("Login")
        self.loginButton.setFixedSize(100, 45)  # Define o tamanho fixo do botão (200 pixels de largura por 50 pixels de altura)
        self.loginButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")  # Define a cor de fundo como azul e a cor do texto como branco
        self.loginButton.clicked.connect(lambda: self.send_data_to_server(user_session))
        self.layout.addWidget(self.loginButton)
        self.setLayout(self.layout)

        # Botão cadastrar
        self.cadastrarButton = QPushButton("Cadastrar")
        self.cadastrarButton.setFixedSize(100, 45)  # Define o tamanho fixo do botão (200 pixels de largura por 50 pixels de altura)
        self.cadastrarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")  # Define a cor de fundo como azul e a cor do texto como branco
        self.cadastrarButton.clicked.connect(self.cadastrarClicked)
        self.layout.addWidget(self.cadastrarButton)
        self.setLayout(self.layout)

        # Configuração do grid layout
        self.gridLayout.addWidget(self.emailLabel, 1, 1)
        self.gridLayout.addWidget(self.emailInput, 2, 1)
        self.gridLayout.addWidget(self.senhaLabel, 3, 1)
        self.gridLayout.addWidget(self.senhaInput, 4, 1)
        self.gridLayout.addWidget(self.loginButton, 7, 1, alignment=Qt.AlignCenter)
        self.gridLayout.addWidget(self.logoLabel, 7, 0, alignment=Qt.AlignCenter)  # Posição da logo na grade
        self.gridLayout.addWidget(self.cadastrarLabel, 8, 0)
        self.gridLayout.addWidget(self.cadastrarButton, 8, 1, alignment=Qt.AlignCenter)

        # Adiciona os widgets ao layout principal
        self.layout.addLayout(self.gridLayout)
        #layout.addWidget(loginButton)

        self.setLayout(self.layout)