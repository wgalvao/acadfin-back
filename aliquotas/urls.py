from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AliquotaViewSet

router = DefaultRouter()
router.register(r'aliquotas', AliquotaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('aliquotas/user/<int:user_id>/',
         AliquotaViewSet.as_view({'get': 'list_by_user'}), name='aliquota-list-by-user'),
]
