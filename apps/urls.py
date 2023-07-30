from django.urls import path

from apps.views import IndexView, BaseView
from apps.events.views import EventsView, EventDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('events/', EventsView.as_view(), name='events'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('base/', BaseView.as_view(), name='base'),
]
