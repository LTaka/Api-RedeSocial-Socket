from PySide6.QtWidgets import (
    QWidget,
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

class Publication(QWidget):
    def __init__(self, user_session, id_publication, id_community, parent=None):
        super().__init__(parent)
        self.id_publication = id_publication
        self.id_community = id_community
        self.setWindowTitle("Publicacao")
        self.setupUI(user_session)
        
    def visualizarPerfilClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.profile()

    def logoutClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.logout()

    def voltarClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.community(self.id_community)

    # def likeClicked(self):
    #     print("like")

    def getIDPublication(self):
        publicationGetByid = {'method':'GET',
                    'entity':'publication',
                    'type':'byID',
                    'value':self.id_publication}
        socket = Connect()
        return socket.typeConnect(publicationGetByid)        

    def setupUI(self, user_session):
        layout = QVBoxLayout(self)
        self.resize(600, 400)  # Define o tamanho da janela para

        # Linha 0 - Botões
        buttonsLayout = QHBoxLayout()

        #Botão atualizar
        atualizarButton = QPushButton("Atualizar")
        atualizarButton.setFixedSize(70, 25)
        atualizarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        atualizarButton.clicked.connect(self.atualizar_pagina)

        #Botão voltar
        voltarButton = QPushButton("Voltar")
        voltarButton.setFixedSize(70, 25)
        voltarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        voltarButton.clicked.connect(self.voltarClicked)
        
        #Botão adicionar comunidade
        self.adicionarButton = QPushButton("Adicionar Comentario")
        self.adicionarButton.setFixedSize(200, 25)
        self.adicionarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        
        #Botão visualizar perfil
        perfilButton = QPushButton("Visualizar Perfil")
        perfilButton.setFixedSize(150, 25)
        perfilButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        perfilButton.clicked.connect(self.visualizarPerfilClicked)

        responseTitle = self.getIDPublication()
        public=responseTitle["description"]
        publicacaoButton = QPushButton("Texto publicação")
        publicacaoButton.setText( public)
        publicacaoButton.setFixedSize(250, 50)
        publicacaoButton.setStyleSheet("background-color: black ; color: #EEAE2D; border-radius: 10px;")

        buttonsLayout.addWidget(voltarButton)
        buttonsLayout.addWidget(atualizarButton)
        buttonsLayout.addWidget(self.adicionarButton)
        buttonsLayout.addWidget(perfilButton)
    
        layout.addLayout(buttonsLayout)

        buttonPublicarion = QHBoxLayout()
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        buttonPublicarion.addItem(spacerItem)
        buttonPublicarion.addWidget(publicacaoButton, alignment=Qt.AlignCenter)
        layout.addLayout(buttonPublicarion)

        # Botões (Comunidades) com scroll
        self.scrollArea = QScrollArea()
        scrollContent = QWidget()
        scrollLayout = QVBoxLayout(scrollContent)

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

        # Conectar o botão "Adicionar Publicação" ao slot correspondente
        self.adicionarButton.clicked.connect(partial(self.sendPost, user_session))
        
        self.atualizar_pagina()
        
    def atualizar_pagina(self):        
        #criando requisicao
        commentsGet = {'method':'GET',
                           'entity':'comment',
                           'type':'all',
                            'value':self.id_publication
                           }
        socket = Connect()
        comments = socket.typeConnect(commentsGet)

        # apaga dados ja existentes
        self.clearScrollArea()

        # inclui comentarios atualizados
        for comment in comments:
            commentButton = QPushButton("descrição")
            commentButton.setText(comment['description'])
            commentButton.setFixedSize(QSize(350, 75))
            commentButton.setStyleSheet("background-color: white; color: black; border-radius: 10px; border: 1px solid #EEAE2D;")
            self.scrollArea.widget().layout().addWidget(commentButton, alignment=Qt.AlignCenter)

    def clearScrollArea(self):
        scrollContent = self.scrollArea.widget()
        if scrollContent is not None and scrollContent.layout() is not None:
            while scrollContent.layout().count():
                item = scrollContent.layout().takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def sendPost (self, user_session):
        commentDescription, ok= QInputDialog.getText(self, "Inserir comentario", "Comente:")
        if ok and commentDescription:
            commentPost = {'method': 'POST',
                            'usage': 'comment_register',
                            'id_user': user_session.get_user_id(),
                            'id_publication': self.id_publication,
                            'description': commentDescription}
            socket = Connect()
            response = socket.typeConnect(commentPost)

        self.atualizar_pagina()