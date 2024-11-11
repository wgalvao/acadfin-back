from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JornadaViewSet

router = DefaultRouter()
router.register(r'jornadas', JornadaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
