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
    QSizePolicy, 
    QMessageBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
from functools import partial
from connect import Connect

class Community(QWidget):
    def __init__(self, user_session, id_community, parent=None):
        super().__init__(parent)
        self.id_community = id_community
        self.setupUI(user_session)
    
    def entrarComunidadeClicked(self, user_session):
        post_user_enter_community = {'method':'POST',
                                     'usage':'user_register_community',
                                     'id_user':user_session.get_user_id(),
                                     'id_community':self.id_community}
        socket=Connect()
        socket.typeConnect(post_user_enter_community)
        self.entrarButton.setStyleSheet("background-color: gray; color: black; border-radius: 10px;")

        self.atualizar_pagina(user_session)

    def logoutClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.logout()

    def voltarClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.home()

    def likeClicked(self, id_publication, user_session):
        userCommunityResponse = self.getUserCommunity(user_session)
        # resgata os ids para efetuar verificacao 
        user_communities = [c['id_community'] for c in userCommunityResponse]
        if (self.id_community not in user_communities):
            QMessageBox.warning(self, "Erro de Publicação", "Você precisa entrar na comunidade para curtir uma publicação")
        else:
            post_like = {'method':'POST',
                        'usage':'like',
                        'id_publication':id_publication,
                        'id_user':user_session.get_user_id()}
            socket = Connect()
            socket.typeConnect(post_like)

            self.atualizar_pagina(user_session)

    def publicationClicked(self, id_publication, user_session):
        userCommunityResponse = self.getUserCommunity(user_session)

        # resgata os ids para efetuar verificacao
        user_communities = [c['id_community'] for c in userCommunityResponse]
        if (self.id_community not in user_communities):
            QMessageBox.warning(self, "Erro de Publicação", "Você precisa entrar na comunidade para visualizar a publicação")
        else:
            main_window = self.parent().parent()  # Obtenha a instância de MainWindow
            main_window.publication(id_publication, self.id_community)

    def getUserCommunity(self, user_session):
        # verifica se usuário esta na comunidade
        getUserCommunity = {'method':'GET',
                            'entity':'community',
                            'type':'all',
                            'value':user_session.get_user_id()}
        socket = Connect()

        return socket.typeConnect(getUserCommunity)

    def setupUI(self, user_session):
        layout = QVBoxLayout(self)
        self.resize(600, 400)  # Define o tamanho da janela para
        self.setWindowTitle("Comunidade")

        # Linha 0 - Botões
        buttonsLayout = QHBoxLayout()

        #Botão atualizar
        atualizarButton = QPushButton("Atualizar")
        atualizarButton.setFixedSize(70, 25)
        atualizarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        atualizarButton.clicked.connect(lambda: self.atualizar_pagina(user_session))

        #Botão voltar
        voltarButton = QPushButton("Voltar")
        voltarButton.setFixedSize(70, 25)
        voltarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        voltarButton.clicked.connect(self.voltarClicked)
        
        #Botão adicionar comunidade
        self.adicionarButton = QPushButton("Adicionar Publicação")
        self.adicionarButton.setFixedSize(200, 25)
        self.adicionarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        
        #Botão entrar na comunidade perfil
        self.entrarButton = QPushButton("Entrar na Comunidade")
        self.entrarButton.setFixedSize(150, 25)
        
        userCommunityResponse = self.getUserCommunity(user_session)

        # resgata os ids para efetuar verificacao
        user_communities = [c['id_community'] for c in userCommunityResponse]

        if self.id_community in user_communities:
            self.entrarButton.setStyleSheet("background-color: gray; color: black; border-radius: 10px;")
        else:
            self.entrarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
            self.entrarButton.clicked.connect(partial(self.entrarComunidadeClicked, user_session))

        buttonsLayout.addWidget(voltarButton)
        buttonsLayout.addWidget(atualizarButton)
        buttonsLayout.addWidget(self.adicionarButton)
        buttonsLayout.addWidget(self.entrarButton)

        layout.addLayout(buttonsLayout)

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

        # Conectar o botão "Adicionar Comunidade" ao slot correspondente
        self.adicionarButton.clicked.connect(partial(self.sendPost, user_session))
        
        self.atualizar_pagina(user_session)
        
    def atualizar_pagina(self, user_session):
        #criando requisicao
        publicationGet = {'method':'GET',
                           'entity':'publication',
                           'type':'all',
                            'value':self.id_community
                           }
        socket = Connect()
        publications = socket.typeConnect(publicationGet)

        # apaga dados ja existentes
        self.clearScrollArea()

        # inclui publicacoes atualizadas
        for publication in publications:
            publicationButton = QPushButton("Descricao")
            publicationButton.setText(publication['description'])
            publicationButton.setFixedSize(QSize(470, 75))
            publicationButton.setStyleSheet("background-color: white; color: black; border-radius: 10px; border: 1px solid #EEAE2D;")
            self.scrollArea.widget().layout().addWidget(publicationButton, alignment=Qt.AlignLeft)
            publicationButton.clicked.connect(partial(self.publicationClicked, publication['id_publication'], user_session))
            
            likeButton = QPushButton("like")
            likeButton.setText('Likes: ' + str(publication['likes_amount']))
            likeButton.setFixedSize(QSize(75, 30))
            likeButton.setStyleSheet("background-color: #289fc5; color: black; border-radius: 5px; border: 1px solid black;")
            likeButton.clicked.connect(partial(self.likeClicked, publication['id_publication'], user_session))
            self.scrollArea.widget().layout().addWidget(likeButton, alignment=Qt.AlignRight)

    def clearScrollArea(self):
        scrollContent = self.scrollArea.widget()
        if scrollContent is not None and scrollContent.layout() is not None:
            while scrollContent.layout().count():
                item = scrollContent.layout().takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def sendPost(self, user_session):
        userCommunityResponse = self.getUserCommunity(user_session)

        # resgata os ids para efetuar verificacao
        user_communities = [c['id_community'] for c in userCommunityResponse]
        if (self.id_community not in user_communities):
            QMessageBox.warning(self, "Erro de Publicação", "Você precisa entrar na comunidade antes de publicar")
        else:
            publicationDescription, ok = QInputDialog.getText(self, "Inserir a Publicação", "Publique:")
            if ok and publicationDescription:
                publicationPost = {'method': 'POST',
                                'usage': 'publication_register',
                                'id_user': user_session.get_user_id(),
                                'id_community': self.id_community,
                                'description': publicationDescription}
                socket = Connect() 
                response = socket.typeConnect(publicationPost)

            self.atualizar_pagina(user_session)
