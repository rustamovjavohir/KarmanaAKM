from django.urls import path

from api.events.views import EventsListAPIView


urlpatterns = [
    path('list/', EventsListAPIView.as_view(), name='events-list'),
]