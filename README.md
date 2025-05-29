# Como Executar esta API

  

Siga os passos abaixo para executar a API localmente:

  

1. **Clone o repositório**

```bash

git clone https://github.com/arthurmnz/backend-TISS

cd backend-TISS

```

2. **Instale as dependências**

	***- use o poetry***
```bash

poetry install

```

3. **Entre no ambiente**

```bash
poetry env activate
```

4. **Configure seu .env**

```.env
DJANGO_SECRET_KEY=seu_token_super_secreto
DJANGO_DEBUG=1

DB_NAME=TISS
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
``` 

5. **Execute a API**

- Realize as migrações do banco de dados:

```bash

poetry run python manage.py makemigrations

```

- Aplique as migrações:

```bash

poetry run python manage.py migrate

```

- Inicie o servidor de desenvolvimento:

```bash

poetry run python manage.py runserver

```