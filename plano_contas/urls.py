from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanoContasViewSet

router = DefaultRouter()
router.register(r'plano-contas', PlanoContasViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('plano-contas/user/<int:user_id>/',
         PlanoContasViewSet.as_view({'get': 'list_by_user'}), name='plano-conta-list-by-user'),
]
