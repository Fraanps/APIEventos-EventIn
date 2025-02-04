# API de Eventos com Django

Este é um projeto acadêmico para a criação de uma API de gerenciamento de eventos utilizando **Django** e **Django REST Framework**.

## 🚀 Tecnologias Utilizadas

- **[Django](https://www.djangoproject.com/):** Framework web de alto nível para Python.
- **[Django REST Framework](https://www.django-rest-framework.org/):** Ferramenta poderosa para criação de APIs RESTful.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- [Python 3.9+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (opcional, mas recomendado)

## 🛠️ Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/api-eventos.git
   cd api-eventos
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações do banco de dados:**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário para acessar o painel administrativo:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```
   A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 📂 Estrutura do Projeto

```plaintext
.
├── eventos/                # Aplicação principal
│   ├── migrations/         # Migrações do banco de dados
│   ├── models.py           # Modelos do Django
│   ├── serializers.py      # Serializadores para a API
│   ├── views.py            # Views da API
│   ├── urls.py             # Rotas da API
│
├── manage.py               # Gerenciador do Django
├── db.sqlite3              # Banco de dados SQLite (apenas para desenvolvimento)
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

## 🧪 Testes

Para rodar os testes automatizados, utilize o comando:
```bash
python manage.py test
```

## 🚀 Endpoints Principais

- `GET /eventos/` - Lista todos os eventos.
- `POST /eventos/` - Cria um novo evento.
- `GET /eventos/{id}/` - Obtém detalhes de um evento específico.
- `PUT /eventos/{id}/` - Atualiza um evento existente.
- `DELETE /eventos/{id}/` - Remove um evento.

## 🔑 Autenticação

A API utiliza autenticação baseada em Token. Para obter um token de autenticação, faça uma requisição para:
```bash
POST /api/token/
```
Enviando um payload com **username** e **password**.

