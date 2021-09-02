http://berinfontes.com

## Setup dev

O projeto pode precisar do Postgres para executar. Então por isso, é necessário instalar alguns pacotes com `sudo apt install python3-dev libpq-dev build-essential postgresql postgresql-contrib`.

Outra dependência é o Node.js para rodar o [sass](https://www.npmjs.com/package/sass). Para instalar o npm, siga [este guia](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-20-04-pt).

Depois do postgres instalado, siga com:

1.  Instalar o [pyenv](https://github.com/pyenv/pyenv-installer);
2.  Instalar o Python 3.8 com `pyenv install 3.8.10`:
3.  Clonar o repositório: `git@github.com:berinhard/berinfontes.com.git`;
4.  Criar o ambiente virtual Python: `pyenv virtualenv 3.8.10 berinfontes.com`;
5.  Ativar o ambiente virtual `pyenv activate berinfontes.com`;
6.  Entrar no diretório do projeto: `cd berinfontes.com`;
7.  Instalar dependencias `pip install -r requirements.txt`;
8.  Copiar o arquivo com variáveis de ambiente: `cp env.example .env`;
9.  Rodar as migrações: `make migrate`;
10. Instalar o sass e dependências de front com `npm install`;

## Rodando o projeto

Para rodar o projeto, são necessários dois comandos que rodam separados em 2 sessões do terminal.
Para rodar ambos você precisará ter o virtualenv ativado como demonstrado acima.

`make serve`: comando para levantar o site localmente que poderá ser acessado em
http://localhost:8000;
`make scss_watch`: comando para atualizar o arquivo `style.css` aa partir do arquivo em
`project/static/sass/style.scss`;

## Acessando o admin

Para criar um usuário administrativo para logar no admin rode o comando:

`python project/manage.py createsuperuser`
