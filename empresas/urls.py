from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmpresaViewSet


router = DefaultRouter()
router.register(r'empresas', EmpresaViewSet)

# urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
    path('empresas/user/<int:user_id>/',
         EmpresaViewSet.as_view({'get': 'list_by_user'}), name='empresa-list-by-user'),
    # path('empresas/<int:user_id>/',
    #  EmpresaViewSet.as_view({'get': 'list_by_user'}), name = 'empresa-list-by-user'),
]
