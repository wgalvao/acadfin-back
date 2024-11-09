from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CadCentroDeCustosViewSet

router = DefaultRouter()
router.register(r'centro-de-custos', CadCentroDeCustosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
