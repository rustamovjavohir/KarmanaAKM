from apps.writers.views import WritersView, WritersDetailView
from django.urls import path

urlpatterns = [
    path('', WritersView.as_view(), name='writers'),
    path('<slug:slug>/', WritersDetailView.as_view(), name='writers-detail'),
]
