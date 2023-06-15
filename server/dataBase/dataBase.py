import sqlite3
import os

class DB:
    def __init__(self) -> None:
        #  os.getcwd() retorna o diretório de trabalho atual
        dbUrlLocation = os.getcwd() + '/server/dataBase/dataBase.db'
        # Conectando ao banco de dados SQLite
        self.db = sqlite3.connect(dbUrlLocation)
    pass