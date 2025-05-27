# Como Executar esta API

Siga os passos abaixo para executar a API localmente:

1. **Clone o repositório**
    ```bash
    git clone https://github.com/arthurmnz/backend-TISS
    cd backend-TISS
    ```

2. **Crie e ative um ambiente virtual**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure seu .env**
    ```.env
        DB_NAME=TISS
        DB_USER=postgres
        DB_PASSWORD=sua_senha
        DB_HOST=localhost
        DB_PORT=5432
        DJANGO_SECRET_KEY=seu_token_super_secreto
        DJANGO_DEBUG=1
    ``` 
    
5. **Execute a API**

    - Realize as migrações do banco de dados:
    ```bash
    python manage.py makemigrations
    ```

    - Aplique as migrações:
    ```bash
    python manage.py migrate
    ```

    - Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```
