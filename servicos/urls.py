from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CadServicoViewSet

router = DefaultRouter()
router.register(r'servicos', CadServicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('servicos/user/<int:user_id>/',
         CadServicoViewSet.as_view({'get': 'list_by_user'}), name='servico-list-by-user'),
]
