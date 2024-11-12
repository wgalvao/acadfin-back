from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AcumuladorViewSet

router = DefaultRouter()
router.register(r'acumuladores', AcumuladorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
