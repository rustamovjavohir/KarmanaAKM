from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.urls import path
from django.views.decorators.cache import cache_page

from apps.views import IndexView, BaseView, index
from apps.events.views import EventsView, EventDetailView
from apps.writers.views import WritersView, WritersDetailView
from config import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

urlpatterns = [
    path('', cache_page(CACHE_TTL)(IndexView.as_view()), name='index'),  # cache_page(CACHE_TTL)(index)
    path('events/', EventsView.as_view(), name='events'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('writers/', WritersView.as_view(), name='writers'),
    path('writers/<slug:slug>/', WritersDetailView.as_view(), name='writers-detail'),
    path('base/', BaseView.as_view(), name='base'),
]
