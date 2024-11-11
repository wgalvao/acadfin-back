from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BaseCalculoViewSet

router = DefaultRouter()
router.register(r'base-calculos', BaseCalculoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
