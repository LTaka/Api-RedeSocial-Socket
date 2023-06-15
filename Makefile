# Nome do ambiente virtual
VENV_NAME := myenv

# Comando para criar o ambiente virtual
ifeq ($(OS),Windows_NT)
    VENV_CREATE := python -m venv $(VENV_NAME)
else
    ifeq ($(shell command -v python3 2> /dev/null),)
        VENV_CREATE := $(PYTHON) -m venv $(VENV_NAME)
    else
        VENV_CREATE := python3 -m venv $(VENV_NAME)
    endif
endif

# Comando para ativar o ambiente virtual
ifeq ($(OS),Windows_NT)
    VENV_ACTIVATE := $(VENV_NAME)\Scripts\activate
else
    VENV_ACTIVATE := . $(VENV_NAME)/bin/activate
endif

# Comando para atualizar o pip
PIP_UPGRADE := $(VENV_ACTIVATE) && python -m pip install --upgrade pip

# Comando para instalar as dependências
INSTALL_DEPENDENCIES := $(VENV_ACTIVATE) && pip install -r requirements.txt

# Comando para executar o servidor
RUN_SERVER := $(VENV_ACTIVATE) && python server/server.py

# Comando para executar o cliente
RUN_CLIENT := $(VENV_ACTIVATE) && python client/client.py

RUN_APP := $(VENV_ACTIVATE) && python3 client/app.py

# Regra padrão do Makefile (executa o projeto)
all: run

# Regra para criar o ambiente virtual
venv:
	$(VENV_CREATE)

# Regra para ativar o ambiente virtual e atualizar o pip
activate:
	$(VENV_ACTIVATE) && $(PIP_UPGRADE)

# Regra para instalar as dependências
install:
	$(INSTALL_DEPENDENCIES)

# Regra para executar o servidor
run_server:
	$(RUN_SERVER)

# Regra para executar o cliente
run_client:
	$(RUN_CLIENT)

clean:
	$(shell rmdir /s /q $(VENV_NAME))