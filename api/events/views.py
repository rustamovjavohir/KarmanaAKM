from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from api.events.filters import EventFilter
from api.events.paginations import EventsPagination
from apps.events.models import Events
from rest_framework.generics import ListAPIView
from api.events.serializers import EventSerializer
from django_filters.rest_framework import DjangoFilterBackend


class EventsListAPIView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Events.objects.filter(is_active=True).order_by('-created_at')
    permission_classes = (AllowAny,)
    pagination_class = EventsPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name', "description"]
    filterset_class = EventFilter

