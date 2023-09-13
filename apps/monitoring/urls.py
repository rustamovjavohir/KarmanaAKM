from apps.monitoring.views import MonitoringView
from django.urls import path

urlpatterns = [
    path('', MonitoringView.as_view(), name='monitoring'),
]
