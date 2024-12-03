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
