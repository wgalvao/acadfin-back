# Acadfin - Sistema de Informação Contábil

Acadfin é um sistema de backend desenvolvido em Django REST Framework (DRF) com autenticação baseada em tokens JWT (Simple JWT) para gerenciar informações contábeis. Este projeto foi desenvolvido como parte da disciplina de Sistemas de Informações Contábeis da Universidade Estadual do Tocantins (UNITINS).

## Funcionalidades

- **Cadastro de Usuários e Autenticação**: Gerenciamento seguro de usuários com autenticação baseada em Simple JWT.
- **Gerenciamento de Contas e Lançamentos Contábeis**: CRUD para manipulação de dados contábeis, incluindo contas, lançamentos, relatórios financeiros, e muito mais.
- **Controle de Acesso**: Utilização de permissões para proteger dados e funcionalidades específicas.

## Requisitos

- Python 3.8+
- Django 4.x
- Django REST Framework
- Simple JWT

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/usuario/acadfin.git
   cd acadfin
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente, incluindo as chaves do JWT e as configurações do banco de dados em `.env`.

5. Aplique as migrações:

   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário para acesso administrativo:
   ```bash
   python manage.py createsuperuser
   ```

## Uso

Para iniciar o servidor de desenvolvimento, execute:

```bash
python manage.py runserver
```

## Endpoints Principais

```bash
api/auth/login/ - Login com Simple JWT.
api/empreaas/ - Gerenciamento de contas contábeis.
api/lancamentos/ - Lançamentos contábeis.
```

> Acesse o servidor local em http://127.0.0.1:8000/.

## Documentação

A documentação da API pode ser acessada diretamente na aplicação através do drf_yasg em /swagger/ e /redoc/ após configurar as dependências necessárias para Swagger.

## Tecnologias Utilizadas

Django: Framework de desenvolvimento web.
Django REST Framework: Criação de APIs RESTful robustas.
Simple JWT: Gerenciamento de autenticação JWT.
Contribuição
Contribuições são bem-vindas. Para contribuir, faça um fork deste repositório, crie uma branch para suas alterações e abra um pull request.

## Licença

Este projeto é desenvolvido para fins acadêmicos como parte do curso de Sistemas de Informações Contábeis na UNITINS.
