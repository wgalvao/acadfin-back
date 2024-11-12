from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlanoContasViewSet

router = DefaultRouter()
router.register(r'plano-contas', PlanoContasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
