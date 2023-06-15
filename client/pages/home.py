from PySide6.QtWidgets import (
    QWidget, 
    QLabel, 
    QVBoxLayout, 
    QPushButton, 
    QHBoxLayout, 
    QScrollArea, 
    QInputDialog, 
    QSpacerItem, 
    QSizePolicy
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
from functools import partial
from connect import Connect

class Home(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Campus UniVerse")
        self.setupUI()
    
    def visualizarPerfilClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.profile()

    def logoutClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.logout()

    def buscarClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.search()

    def communityClicked(self, id_community):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.community(id_community)

    def setupUI(self):
        layout = QVBoxLayout(self)
        self.resize(600, 400)  # Define o tamanho da janela para

        # Linha 0 - Botões
        buttonsLayout = QHBoxLayout()

        #Botão atualizar
        atualizarButton = QPushButton("Atualizar")
        atualizarButton.setFixedSize(70, 25)
        atualizarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        atualizarButton.clicked.connect(self.atualizar_pagina)

        #Botão buscar
        buscarButton = QPushButton("Buscar")
        buscarButton.setFixedSize(70, 25)
        buscarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        buscarButton.clicked.connect(self.buscarClicked)
        
        #Botão adicionar comunidade
        self.adicionarButton = QPushButton("Adicionar Comunidade")
        self.adicionarButton.setFixedSize(200, 25)
        self.adicionarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        
        #Botão visualizar perfil
        perfilButton = QPushButton("Visualizar Perfil")
        perfilButton.setFixedSize(150, 25)
        perfilButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        perfilButton.clicked.connect(self.visualizarPerfilClicked)

        # buttonsLayout.addWidget(voltarButton)
        buttonsLayout.addWidget(atualizarButton)
        buttonsLayout.addWidget(buscarButton)
        buttonsLayout.addWidget(self.adicionarButton)
        buttonsLayout.addWidget(perfilButton)

        layout.addLayout(buttonsLayout)

        # Botões (Comunidades) com scroll
        self.scrollArea = QScrollArea()
        scrollContent = QWidget()
        self.scrollLayout = QVBoxLayout(scrollContent)

        self.atualizar_pagina()  # inicializa comunidades
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(scrollContent)
        layout.addWidget(self.scrollArea)

        # Última linha - Logout
        logoutButton = QPushButton("Logout")
        layout.addWidget(logoutButton, alignment=Qt.AlignRight)
        logoutButton.setFixedSize(70, 25)
        logoutButton.setStyleSheet("background-color: #B22222; color: black; border-radius: 10px;")
        logoutButton.clicked.connect(self.logoutClicked)


        # Última linha - Imagem e Nome da Página
        bottomLayout = QHBoxLayout()

        # Adicionar um espaçador à esquerda
        leftSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        bottomLayout.addSpacerItem(leftSpacer)

        imageLabel = QLabel()
        pixmap = QPixmap("client/images/logob.png")

        pageNameLabel = QLabel("Campus UniVerse")
        width = 20  # Largura desejada
        height = 20  # Altura desejada
        scaledPixmap = pixmap.scaled(width, height)
        imageLabel.setPixmap(scaledPixmap)  

        bottomLayout.addWidget(imageLabel)
        bottomLayout.addWidget(pageNameLabel)

        # Adicionar um espaçador à direita
        rightSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        bottomLayout.addSpacerItem(rightSpacer)

        layout.addLayout(bottomLayout)

        self.setLayout(layout)

        # Conectar o botão "Adicionar Comunidade" ao slot correspondente
        self.adicionarButton.clicked.connect(self.showCommunityInputDialog)
        
    def atualizar_pagina(self):
        get_community = {'method': 'GET',
                        'entity': 'community',
                        'type': 'all',
                        'value': None}
        socket=Connect()
        community_response = socket.typeConnect(get_community)

        # apaga dados ja existentes
        self.clearScrollArea()

        for community in community_response:        
            communityButton = QPushButton(community['name'])
            communityButton.setFixedSize(QSize(460, 75))
            communityButton.setStyleSheet("background-color: white; color: black; border-radius: 10px; border: 1px solid black;")
            communityButton.clicked.connect(partial(self.communityClicked, community['id_community']))
            self.scrollLayout.addWidget(communityButton, alignment=Qt.AlignCenter)
        
    def clearScrollArea(self):
        scrollContent = self.scrollArea.widget()
        if scrollContent is not None and scrollContent.layout() is not None:
            while scrollContent.layout().count():
                item = scrollContent.layout().takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def showCommunityInputDialog(self):
        # Exibir a caixa de diálogo de entrada de texto para inserir o nome da comunidade
        communityName, ok = QInputDialog.getText(self, "Inserir Nome da Comunidade", "Nome da Comunidade:")

        if ok and communityName:
            # Criar um botão com o nome da comunidade e adicioná-lo ao layout
            communityButton = QPushButton(communityName)
            communityButton.setFixedSize(QSize(350, 75))
            communityButton.setStyleSheet("background-color: white; color: black; border-radius: 10px; border: 1px solid black;")
            self.scrollArea.widget().layout().addWidget(communityButton, alignment=Qt.AlignCenter)
            communityPost = {'method':'POST',
                             'usage':'community_register',
                             'name':communityName}
            socket = Connect()
            postResponse = socket.typeConnect(communityPost)

        # atualiza a pagina apos a insercao
        self.atualizar_pagina()