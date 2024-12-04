from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FuncaoViewSet

router = DefaultRouter()
router.register(r'funcoes', FuncaoViewSet, basename='funcao')

urlpatterns = [
    path('', include(router.urls)),
    path('funcoes/user/<int:user_id>/',
         FuncaoViewSet.as_view({'get': 'list_by_user'}), name='funcoe-list-by-user'),
]
