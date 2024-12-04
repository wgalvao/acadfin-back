from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CfopViewSet

router = DefaultRouter()
router.register(r'cfops', CfopViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cfops/user/<int:user_id>/',
         CfopViewSet.as_view({'get': 'list_by_user'}), name='cfop-list-by-user'),
]
