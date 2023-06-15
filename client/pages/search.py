from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QScrollArea, 
    QWidget, 
    QVBoxLayout, 
    QHBoxLayout, 
    QLabel, 
    QLineEdit, 
    QPushButton, 
    QFrame
)
from PySide6.QtCore import Qt, QSize
from connect import Connect
from functools import partial

class Search(QWidget):
    def __init__(self, user, parent=None):
        super().__init__(parent)
        self.user = user
        self.setWindowTitle("Publicacao")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.resize(600, 400)  # Define o tamanho da janela para

        # Linha 0 - Botões
        buttonsLayout = QHBoxLayout() # Layout horizontal para colocar os elementos na mesma linha

        #Botão voltar
        voltarButton = QPushButton("Voltar")
        voltarButton.setFixedSize(70, 25)
        voltarButton.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        voltarButton.clicked.connect(self.voltarClicked)

        # Cria a caixa de entrada
        self.search_bar = QLineEdit()

        # Cria o botão de pesquisa
        comunidade_button = QPushButton("Comunidade")
        comunidade_button.setFixedSize(70, 25)
        comunidade_button.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        comunidade_button.clicked.connect(self.comunidade_search)


        # Cria o botão de limpar
        pessoas_button = QPushButton("Pessoas")
        pessoas_button.setFixedSize(70, 25)
        pessoas_button.setStyleSheet("background-color: #EEAE2D; color: black; border-radius: 10px;")
        pessoas_button.clicked.connect(self.pessoas_search)



        buttonsLayout.addWidget(voltarButton)
        buttonsLayout.addWidget(self.search_bar)
        buttonsLayout.addWidget(comunidade_button)
        buttonsLayout.addWidget(pessoas_button)
    
        layout.addLayout(buttonsLayout)

         # Botões (Comunidades) com scroll
        self.scrollArea = QScrollArea()
        scrollContent = QWidget()
        scrollLayout = QVBoxLayout(scrollContent)

        # self.addpublicationButton(scrollLayout)  # Adicionar um botão de comunidade inicial
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(scrollContent)
        layout.addWidget(self.scrollArea)


    def clearScrollArea(self):
        scrollContent = self.scrollArea.widget()
        if scrollContent is not None and scrollContent.layout() is not None:
            while scrollContent.layout().count():
                item = scrollContent.layout().takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def communityClicked(self, id_community):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.community(id_community)

    def comunidade_search(self):
        self.clearScrollArea()
        search_text = self.search_bar.text().lower()  # Converte o texto da pesquisa para minúsculas
        self.search_bar.clear()
        # Realiza a busca no banco de dados
        get_user = {'method': 'GET',
                        'entity': 'community',
                        'type': 'byName',
                        'value': search_text}
        socket=Connect()
        comments = socket.typeConnect(get_user)
        # Verifica se existem resultados da pesquisa
        if comments:
            for comment, id in zip(comments['communities'], comments['id_community']):
                commentButton = QPushButton("Search")
                commentButton.setText(comment)
                commentButton.setFixedSize(QSize(350, 75))
                commentButton.setStyleSheet("background-color: white; color: black; border-radius: 10px; border: 1px solid #EEAE2D;")
                self.scrollArea.widget().layout().addWidget(commentButton, alignment=Qt.AlignCenter)
                commentButton.clicked.connect(partial(self.communityClicked, id))
        else:
            result_label = QLabel("Nenhum resultado encontrado.")
            self.scrollArea.widget().layout().addWidget(result_label, alignment=Qt.AlignCenter)

    def pessoas_search(self):
        self.clearScrollArea()
        search_text = self.search_bar.text().lower()  # Converte o texto da pesquisa para minúsculas
        self.search_bar.clear()
        
        # Realiza a busca no banco de dados
        get_user = {'method': 'GET',
                        'entity': 'user',
                        'type': 'byName',
                        'value': search_text}
        socket=Connect()
        usuarios = socket.typeConnect(get_user)
        # Verifica se existem resultados da pesquisa
        if usuarios:
            for usuario in usuarios['user']:
                commentButton = QPushButton("Search")
                commentButton.setText(usuario)
                commentButton.setFixedSize(QSize(350, 75))
                commentButton.setStyleSheet("background-color: white; color: black; border-radius: 10px; border: 1px solid #EEAE2D;")
                self.scrollArea.widget().layout().addWidget(commentButton, alignment=Qt.AlignCenter)
                # commentButton.clicked.connect(lambda checked, id_pub=user_id: self.comentarioClicked(id_pub))
        else:
            result_label = QLabel("Nenhum resultado encontrado.")
            self.scrollArea.widget().layout().addWidget(result_label, alignment=Qt.AlignCenter)


    def voltarClicked(self):
        main_window = self.parent().parent()  # Obtenha a instância de MainWindow
        main_window.home()