from django.urls import path
from apps.events.views import EventsView, EventDetailView

urlpatterns = [
    path('', EventsView.as_view(), name='events'),
    path('<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]
