from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CadSindicatoViewSet

router = DefaultRouter()
router.register(r'sindicatos', CadSindicatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]