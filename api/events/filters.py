import django_filters
from django_filters.rest_framework import FilterSet
from apps.events.models import Events


class EventFilter(FilterSet):
    model = Events
    category = django_filters.CharFilter(field_name='category__slug', lookup_expr='iexact')

    class Meta:
        model = Events
        fields = {
            'name': ['exact'],
            'description': ['exact'],
            'body': ['exact'],
            'date': ['exact'],
            'created_by': ['exact'],
        }
