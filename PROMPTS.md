# Atualização semântica

escreva um script em python que examine todos os arquivos view.py e urls.py em todos os diretórios, exceto: authentication, todo, fornecedores, clientes, tasks e empresas.

## views.py

> em views.py altere o seguinte:

```
 @action(detail=False, methods=['get'])
    def list_by_user(self, request, user_id=None):
        fornecedores = Fornecedor.objects.filter(user_id=user_id)
        serializer = self.get_serializer(fornecedores, many=True)
        return Response(serializer.data)
```

Troque o nome Fornecedor pelo o nome da classe corrente e altere fornecedores pelo nome do objeto correspondente da classe.

Além disso adicione as importações correspondentes:

```
from rest_framework.decorators import action
from rest_framework.response import Response
```

## urls.py

> em urls.py faça o seguinte:

```
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FornecedorViewSet

router = DefaultRouter()
router.register(r'fornecedores', FornecedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('fornecedores/user/<int:user_id>/',
         FornecedorViewSet.as_view({'get': 'list_by_user'}), name='fornecedor-list-by-user'),
]

```

Altere os FornecedorViewSet pelo ViewSet correspondente e em name='fornecedor-list-by-user' troque fornecedor pelo nome correspondente da pasta

# Preparação para código inteiro

Escreva um script em bash que leia todas os diretórios e arquivos .py. Ao final gere um arquivo .md que possua o caminho completo para cada arquivo e o código .py dentro de cada arquivo Além da estrutura do projeto.
