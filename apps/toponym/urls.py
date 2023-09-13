from apps.toponym.views import ToponymListView, ToponymDetailView
from django.urls import path

urlpatterns = [
    path('', ToponymListView.as_view(), name='toponyms'),
    path('<slug:slug>/', ToponymDetailView.as_view(), name='toponyms-detail'),
]
