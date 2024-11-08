from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CadServicoViewSet

router = DefaultRouter()
router.register(r'servicos', CadServicoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
