# Organizador de Estudos - API

## Descrição

API em Flask do projeto **Organizador de Estudos**.

O projeto permite cadastrar, listar, buscar, atualizar e remover atividades acadêmicas, como provas, trabalhos, leituras e entregas.

## Requisitos

- Python instalado na máquina.
- `pip` para instalar as dependências.
- Navegador ou ferramenta de API para acessar a documentação Swagger.

## Instalação

1. Acesse a pasta da API:

```text
cd meu_app_api
```

2. Crie um ambiente virtual:

```text
python -m venv venv
```

3. Ative o ambiente virtual no Windows PowerShell:

```text
.\venv\Scripts\Activate.ps1
```

4. Instale as dependências do projeto:

```text
pip install -r requirements.txt
```

## Como executar

Execute a aplicação com Python:

```text
python app.py
```

Também é possível executar com Flask:

```text
flask run --host 0.0.0.0 --port 5000
```

Com o servidor rodando, acesse:

```text
http://127.0.0.1:5000
```

Esse endereço abre a documentação Swagger da API.

## Uso com o front-end

Para usar a interface web, mantenha esta API em execução e abra o arquivo `index.html` do repositório `meu_app_front` no navegador:

```text
meu_app_front/index.html
```
