"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin  # type: ignore
from django.urls import path, include  # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/', include('todo.urls')),  # Include the todo app's URLs
    path('api/', include('tasks.urls')),
    path('api/', include('funcionarios.urls')),
    path('api/', include('empresas.urls')),  # Inclui as rotas da aplicação
    path('api/', include('sindicatos.urls')),
    path('api/', include('servicos.urls')),
    path('api/', include('centro_de_custos.urls')),
    path('api/', include('cargos.urls')),
    path('api/', include('funcoes.urls')),
    path('api/', include('jornadas.urls')),
]
