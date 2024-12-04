from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FuncionarioViewSet

router = DefaultRouter()
router.register(r'funcionarios', FuncionarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('funcionarios/user/<int:user_id>/',
         FuncionarioViewSet.as_view({'get': 'list_by_user'}), name='funcionario-list-by-user'),
]
