# API de Eventos com Django

Este é um projeto acadêmico para a criação de uma API de gerenciamento de eventos utilizando o framework **Django** e a biblioteca **Django REST Framework**. A API foi documentada utilizando **Swagger**, facilitando sua exploração e integração.

---

## 🚀 Tecnologias Utilizadas

- **[Django](https://www.djangoproject.com/):** Framework web para desenvolvimento rápido e seguro.
- **[Django REST Framework (DRF)](https://www.django-rest-framework.org/):** Conjunto de ferramentas para criação de APIs robustas em Django.
- **[Swagger (drf-yasg)](https://drf-yasg.readthedocs.io/en/stable/):** Geração automática de documentação interativa para a API.

---

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- [Python 3.9+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [Venv](https://docs.python.org/pt-br/3.13/library/venv.html) (opcional, mas recomendado)

---

## 🛠️ Instalação e Configuração

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/api-eventos.git
cd api-eventos
```

### 2. Criação do ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 3. Instalação das dependências
```bash
pip install -r requirements.txt
```

### 4. Aplicação das migrações do banco de dados
```bash
python manage.py migrate
```

### 5. Criação de um superusuário (opcional, para acessar o admin Django)
```bash
python manage.py createsuperuser
```

### 6. Execução do servidor local
```bash
python manage.py runserver
```
A API estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📜 Documentação da API

A documentação interativa da API pode ser acessada através do Swagger:

- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **Redoc:** [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

---

## 📂 Estrutura do Projeto

```plaintext
.
├── .venv                  # Ambiente virtual
├── eventin/               # Aplicação principal
│   ├── models.py          # Modelos do banco de dados
│   ├── serializers.py     # Serialização dos dados
│   ├── views.py           # Lógica das rotas
│   ├── urls.py            # Definição das rotas
│   ├── admin.py           # Configuração do Django Admin
│   ├── validators.py      # Validações
│   ├── tests.py           # Testes automatizados *em implementaçãp
│
├── setup/                 # Configuração do projeto Django
│   ├── settings.py        # Configurações gerais
│   ├── urls.py            # Rotas principais
│   ├── wsgi.py            # Ponto de entrada para o servidor
│
├── requirements.txt       # Dependências do projeto
├── manage.py              # Comando principal do Django
├── README.md              # Documentação do projeto
```

---

## 🧪 Testes

Para rodar os testes automatizados:
```bash
python manage.py test
```
---
