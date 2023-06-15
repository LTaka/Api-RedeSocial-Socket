from PySide6.QtWidgets import  QMainWindow, QStackedWidget
from PySide6.QtCore import QObject
from pages import Enrollment, LoginPage, Home, Search, Profile, Publication, Community

class User(QObject):
    def __init__(self):
        super().__init__()
        self.user_id = None
    
    def set_user_id(self, user_id):# Define o ID do usuário 
        self.user_id = user_id

    def get_user_id(self): # Obtém o ID do usuário
        return self.user_id

# Janela principal
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        # cria session
        self.user_session = User()
        # self.socket = socket
        self.stacked_widget = QStackedWidget()# QStackedWidget: Widget que permite exibir várias páginas em um único espaço
        self.setCentralWidget(self.stacked_widget)

        # inicializa com login
        self.login_page = LoginPage(self.user_session)
        self.stacked_widget.addWidget(self.login_page)

    def cadastro(self):
        self.register_page = Enrollment()
        self.stacked_widget.addWidget(self.register_page) 
        self.stacked_widget.setCurrentWidget(self.register_page)
        self.main_window.show_main_page()

    def login(self):
        self.stacked_widget.setCurrentWidget(self.login_page)
        self.main_window.show_main_page()

    def logout(self):
        self.user_session.set_user_id(None)
        self.stacked_widget.setCurrentWidget(self.login_page)
        self.main_window.show_main_page()
    
    def home(self):
        self.home_page = Home()
        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.setCurrentWidget(self.home_page)
        self.main_window.show_main_page()

    def search(self):
        self.search_page = Search(self.user_session)
        self.stacked_widget.addWidget(self.search_page)
        self.stacked_widget.setCurrentWidget(self.search_page)
        self.main_window.show_main_page()

    def profile(self):
        self.profile_page = Profile(self.user_session)
        self.stacked_widget.addWidget(self.profile_page)
        self.stacked_widget.setCurrentWidget(self.profile_page)
        self.main_window.show_main_page()

    def community(self, id_community):
        self.community_page = Community(self.user_session, id_community)
        self.stacked_widget.addWidget(self.community_page)
        self.stacked_widget.setCurrentWidget(self.community_page)
        self.main_window.show_main_page()
        
    def publication(self, id_publication, id_community):
        self.publication_page = Publication(self.user_session, id_publication, id_community)
        self.stacked_widget.addWidget(self.publication_page)
        self.stacked_widget.setCurrentWidget(self.publication_page)
        self.main_window.show_main_page()