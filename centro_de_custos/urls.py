from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CadCentroDeCustosViewSet

router = DefaultRouter()
router.register(r'centro-de-custos', CadCentroDeCustosViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('centro-de-custos/user/<int:user_id>/',
         CadCentroDeCustosViewSet.as_view({'get': 'list_by_user'}), name='centro-de-custo-list-by-user'),
]
