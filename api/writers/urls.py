from django.urls import path

from apps.writers.views import WritersView


urlpatterns = [
    path('list/', WritersView.as_view(), name='writers-list'),
]