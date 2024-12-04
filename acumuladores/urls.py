from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AcumuladorViewSet

router = DefaultRouter()
router.register(r'acumuladores', AcumuladorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('acumuladores/user/<int:user_id>/',
         AcumuladorViewSet.as_view({'get': 'list_by_user'}), name='acumuladores-list-by-user'),
]
