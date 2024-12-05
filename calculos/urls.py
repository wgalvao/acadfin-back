# calculos/urls.py

from django.urls import path
from .views import calcular_decimo_terceiro

urlpatterns = [
    path('calcular-decimo-terceiro/', calcular_decimo_terceiro, name='calcular-decimo-terceiro'),
]