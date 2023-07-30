from django_filters.rest_framework import FilterSet
from apps.books.models import Category


class CategoryFilter(FilterSet):
    model = Category

    class Meta:
        model = Category
        fields = {
            'name': ['exact'],
            'is_event': ['exact']
        }
