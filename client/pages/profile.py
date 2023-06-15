from PySide6.QtWidgets import (
    QVBoxLayout, 
    QWidget, 
    QPushButton, 
    QLabel, 
    QScrollArea, 
    QHBoxLayout, 
    QGridLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from connect import Connect

class Profile(QWidget):
    def __init__(self, user_session, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Perfil")
        self.setupUI(user_session)

    def logoutClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.logout()

    def backClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.home()

    def getUserInformations(self, user_session):
        user_request = {'method':'GET',
                        'entity':'user',
                        'type': 'byID',
                        'value':user_session.get_user_id()}
        socket = Connect()
        user_response = socket.typeConnect(user_request)

        self.getUserCommunities(user_session)

        return user_response
    
    def getUserCommunities(self, user_session):
        communities_ids_request = {'method':'GET',
                        'entity':'community',
                        'type': 'all',
                        'value':user_session.get_user_id()}
        
        socket = Connect()
        communities_ids_response = socket.typeConnect(communities_ids_request)

        community_list = []

        for community in communities_ids_response:
            community_list.append(community['name'])

        return community_list

    def setupUI(self, user_session):
        mainLayout = QVBoxLayout(self)
        self.resize(600, 400)  # Define o tamanho da janela para

        # Botão Voltar
        backButton = QPushButton("Home")
        backButton.setFixedSize(70, 25)
        backButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        mainLayout.addWidget(backButton, alignment=Qt.AlignLeft)
        backButton.clicked.connect(self.backClicked)

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollContentWidget = QWidget(scrollArea)
        scrollContentLayout = QVBoxLayout(scrollContentWidget)
        
        gridLayout = QGridLayout()
        scrollContentLayout.addLayout(gridLayout)

        scrollArea.setWidget(scrollContentWidget)
        mainLayout.addWidget(scrollArea)

        # Logo e Nome da Página
        topLayout = QHBoxLayout()
        mainLayout.addLayout(topLayout)

        logoLabel = QLabel()
        pixmap = QPixmap("client/images/logob.png")

        nomeLabel = QLabel("Campus UniVerse")
        width = 20  # Largura desejada
        height = 20  # Altura desejada
        scaledPixmap = pixmap.scaled(width, height)
        logoLabel.setPixmap(scaledPixmap)  
        topLayout.addWidget(logoLabel, alignment=Qt.AlignRight)
        topLayout.addWidget(nomeLabel, alignment=Qt.AlignLeft)

        user_data = self.getUserInformations(user_session)

        # Linha 1 - Nome
        nomeTextLabel = QLabel("Nome:")
        gridLayout.addWidget(nomeTextLabel, 1, 0)

        # Linha 2 - Botão do Nome
        nomeButton = QPushButton(user_data['name'])
        gridLayout.addWidget(nomeButton, 2, 0)
        nomeButton.setFixedSize(250, 50)
        nomeButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")

        # Linha 3 - E-mail e Senha
        emailTextLabel = QLabel("E-mail:")
        senhaTextLabel = QLabel("Senha:")
        gridLayout.addWidget(emailTextLabel, 3, 0)
        gridLayout.addWidget(senhaTextLabel, 3, 1)

        # Linha 4 - Botões de E-mail e Senha
        emailButton = QPushButton(user_data['email'])
        senhaButton = QPushButton(user_data['password'])
        gridLayout.addWidget(emailButton, 4, 0)
        gridLayout.addWidget(senhaButton, 4, 1)
        emailButton.setFixedSize(250, 50)
        emailButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        senhaButton.setFixedSize(250, 50)
        senhaButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")

        # Linha 5 - Curso e Universidade
        cursoTextLabel = QLabel("Curso:")
        universidadeTextLabel = QLabel("Universidade:")
        gridLayout.addWidget(cursoTextLabel, 5, 0)
        gridLayout.addWidget(universidadeTextLabel, 5, 1)

        # Linha 6 - Botões de Curso e Universidade
        cursoButton = QPushButton(user_data['course'])
        universidadeButton = QPushButton(user_data['university'])
        gridLayout.addWidget(cursoButton, 6, 0)
        gridLayout.addWidget(universidadeButton, 6, 1)
        cursoButton.setFixedSize(250, 50)
        cursoButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        universidadeButton.setFixedSize(250, 50)
        universidadeButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")

        # Linha 7 - Label Comunidades
        comunidadesLabel = QLabel("Comunidades:")
        scrollContentLayout.addWidget(comunidadesLabel)

        # Linha 8 - Botões das Comunidades
        for community in self.getUserCommunities(user_session):
            communityButton = QPushButton(f"{community}")
            scrollContentLayout.addWidget(communityButton, alignment=Qt.AlignCenter)
            communityButton.setFixedSize(250, 50)
            communityButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")

        # Linha 9 - Botão de Logout
        logoutButton = QPushButton("Logout")
        mainLayout.addWidget(logoutButton, alignment=Qt.AlignRight)
        logoutButton.setFixedSize(70, 25)
        logoutButton.setStyleSheet("background-color: #B22222; color: black; border-radius: 10px;")
        logoutButton.clicked.connect(self.logoutClicked)

        self.setLayout(mainLayout)