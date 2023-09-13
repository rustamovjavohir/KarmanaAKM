from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.urls import path, include
from django.views.decorators.cache import cache_page

from apps.views import IndexView, BaseView, index
from apps.toponym.views import ToponymListView, ToponymDetailView
from apps.monitoring.urls import urlpatterns as monitoring_urls
from apps.events.urls import urlpatterns as events_urls
from apps.writers.urls import urlpatterns as writers_urls
from apps.toponym.urls import urlpatterns as toponym_urls
from config import settings

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

urlpatterns = [
    path('', cache_page(CACHE_TTL)(IndexView.as_view()), name='index'),  # cache_page(CACHE_TTL)(index)
    # path('', IndexView.as_view(), name='index'),  # cache_page(CACHE_TTL)(index)
    path('base/', BaseView.as_view(), name='base'),
    path('events/', include(events_urls)),
    path('writers/', include(writers_urls)),
    path('toponyms/', include(toponym_urls)),
    path('monitoring/', include(monitoring_urls)),
]
