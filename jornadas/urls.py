from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JornadaViewSet

router = DefaultRouter()
router.register(r'jornadas', JornadaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('jornadas/user/<int:user_id>/',
         JornadaViewSet.as_view({'get': 'list_by_user'}), name='jornadas-list-by-user'),
]
