# Organizador de Estudos - API

API em Flask do projeto **Organizador de Estudos**.

Ela permite cadastrar, listar, buscar, atualizar e remover atividades acadêmicas, como provas, trabalhos, leituras e entregas.

## Como executar

Acesse a pasta da API:

```text
cd meu_app_api
```

Crie um ambiente virtual:

```text
python -m venv venv
```

Ative o ambiente virtual:

No Windows PowerShell:

```text
.\venv\Scripts\Activate.ps1
```

Instale as dependencias:

```text
pip install -r requirements.txt
```

Execute a aplicacao:

```text
python app.py
```

Ou execute com Flask:

```text
flask run --host 0.0.0.0 --port 5000
```

Com o servidor rodando:

```text
http://127.0.0.1:5000
```

Esse endereço abre a documentação Swagger da API.

Para usar o front-end, abra no navegador o arquivo `index.html` do repositório `meu_app_front`:

```text
meu_app_front/index.html
```
