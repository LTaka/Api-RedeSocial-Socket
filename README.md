# Campus UniVerse

A seguir, serão apresentados os requisitos e o passo-a-passo para execução do projeto Campus UniVerse.

## Requisitos

- Python 3

## Passo a passo para execução

Para executar o sistema proposto, basta entrar com os seguintes comandos, levando-se em consideração as ressalvas e a ordem apresentada dos comandos:

1. **make venv**

   - Executar o comando acima somente na primeira vez que for executar o sistema, para criar o ambiente virtual.

2. **make activate**

   - Este comando deve ser executado sempre que o usuário abrir o terminal para executar o sistema, para ativar o ambiente virtual.

3. **make install**

   - Este comando deve ser executado somente uma vez, para instalar as dependências necessárias para execução do projeto.

4. **make run_server**

   - Executa o server. Este comando deve preceder, obrigatoriamente, o comando abaixo.

5. **make run_client**
    - Executa o cliente em outro terminal. Este comando deve suceder, obrigatoriamente, o comando acima.

## TODO
* Fazer logo no Figma
* Colocar título nas páginas (Para o usuário identificar qual página ele se encontra)
* Usuário sair da comunidade
    * Botão entrar na comunidade será de acordo com a existência do usuário na comunidade
    * Se ele está na comunidade, mostra "Sair da Comunidade" e fica vermelho
    * Se ele não está na comunidade, mostra "Entrar na Comunidade" e fica verde (definir cor)
    * Caso o usuário clique no botão "Sair da Comunidade": ele sairá da comunidade (excluir linha na tabela communities_has_users)
* Editar Perfil
    * Se der tempo, já que não é prioridade para a disciplina de Sistemas Distribuídos
