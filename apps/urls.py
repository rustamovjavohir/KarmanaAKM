from django.urls import path

from apps.views import IndexView, BaseView
from apps.events.views import EventsView, EventDetailView
from apps.writers.views import WritersView, WritersDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('events/', EventsView.as_view(), name='events'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('writers/', WritersView.as_view(), name='writers'),
    path('writers/<slug:slug>/', WritersDetailView.as_view(), name='writers-detail'),
    path('base/', BaseView.as_view(), name='base'),
]
