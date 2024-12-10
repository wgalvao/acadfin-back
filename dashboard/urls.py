# dashboard/urls.py

from django.urls import path
from .views import dashboard_stats

urlpatterns = [
    # path('dashboard-stats/', dashboard_stats, name='dashboard-stats'),
    path('dashboard-stats/<int:user_id>/', dashboard_stats, name='dashboard-stats'),
]