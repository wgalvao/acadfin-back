# Testes de API

## Auth

```
$ curl -XPOST -H "Content-type: application/json" -d '{
    "token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTY0MTE1NiwiaWF0IjoxNzMxMDM2MzU2LCJqdGkiOiI5ZDgxNzU0ZmE2OTA0YmQ4OTNlMDJjYjFiMTg2ZDIwMiIsInVzZXJfaWQiOjN9.q43D9lyY2t9LTJgJLdmscQnjWV9QVq3U8tqZe3Azgvn9S8a_Jpc_NnnvWhYPJKaum6_W-KHqPcJN84Mu74kceQQ"
  }' 'http://localhost:8000/api/auth/token/refresh/' | jq
```

```
$ curl -XPOST -H "Content-type: application/json" -d '{
    "token": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxMDQ3NzUyLCJpYXQiOjE3MzEwNDQxNTIsImp0aSI6IjY3ZDRmZGIxMzBkMzQyZTZhNzEwOGRjMWYyMjUwYTgwIiwidXNlcl9pZCI6M30.5RZsnWKKpGxOgHGLljKGpHmWdQ6jvjE2B_j7CwOpitC2O3rOEhNsnOnKJesdN3JxDwHHNXmzvHFrwMvy_W3JBA"
  }' 'http://localhost:8000/api/auth/token/verify/' | jq
```

## Centro de custos

```
curl -X POST http://127.0.0.1:8000/api/centro-de-custos/ \
-H "Content-Type: application/json" \
-d '{
    "nome": "Centro de Custos A",
    "descricao": "Descrição do Centro de Custos A",
    "codigo": "CC001",
    "ativo": true
}'
```

## Servicos

```
curl -X POST http://127.0.0.1:8000/api/servicos/ \
-H "Content-Type: application/json" \
-d '{
    "codigo": 123,
    "descricao": "Serviço de Limpeza",
    "valor": 150.00,
    "user_id":3
}'

curl -X PUT http://127.0.0.1:8000/api/servicos/1/ \
-H "Content-Type: application/json" \
-d '{
    "codigo": 1243,
    "descricao": "Serviço de Jantar",
    "valor": 150.00,
    "user_id":3
}'
```

## Sindicatos

> Criar

```
curl -X POST http://127.0.0.1:8000/api/sindicatos/ \
-H "Content-Type: application/json" \
-d '{
    "nome": "Sindicato dos Trabalhadores",
    "endereco": "Rua dos Trabalhadores, 123",
    "telefone": "1234567890"
}'


curl -X PUT http://127.0.0.1:8000/api/sindicatos/1/ \
-H "Content-Type: application/json" \
-d '{
    "nome": "Sindicato dos Trabalhadores Atualizado",
    "endereco": "Rua dos Trabalhadores, 456",
    "telefone": "abc123"
}'
```

> update

```
curl -X PUT http://127.0.0.1:8000/api/sindicatos/1/ \
-H "Content-Type: application/json" \
-d '{
    "nome": "Sindicato dos Trabalhadores Atualizado",
    "endereco": "Rua dos Trabalhadores, 456",
    "telefone": "0987654321"
}'
```

> partial update

```
curl -X PATCH http://127.0.0.1:8000/api/sindicatos/1/ \
-H "Content-Type: application/json" \
-d '{
    "telefone": "1122334455"
}'
```

-H "Authorization: Bearer <your_token>" \

```
curl -X POST http://localhost:8000/api/empresas/ \
-H "Content-Type: application/json" \
-d '{
    "nome_razao": "Tech Solutions Ltda",
    "cnpj": "12.345.678/0001-90",
    "endereco": "Rua das Flores",
    "numero": "123",
    "bairro": "Centro",
    "cidade": "São Paulo",
    "estado": "SP",
    "cep": "01234-567",
    "telefone": "(11)3456-7890",
    "email": "contato@techsolutions.com",
    "preposta": "João Silva"
}'

```
