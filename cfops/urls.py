from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CfopViewSet

router = DefaultRouter()
router.register(r'cfops', CfopViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
