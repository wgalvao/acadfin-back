from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContaViewSet

router = DefaultRouter()
router.register(r'contas', ContaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('contas/user/<int:user_id>/',
         ContaViewSet.as_view({'get': 'list_by_user'}), name='conta-list-by-user'),
]
