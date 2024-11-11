from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AliquotaViewSet

router = DefaultRouter()
router.register(r'aliquotas', AliquotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
