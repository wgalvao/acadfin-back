from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FuncaoViewSet

router = DefaultRouter()
router.register(r'funcoes', FuncaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
