from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from api.books.paginations import BasePagination
from apps.books.models import Image, Category
from rest_framework.generics import ListAPIView, RetrieveAPIView
from api.books.serializers import ImageSerializer, CategorySerializer
from api.books.filters import CategoryFilter


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    pagination_class = BasePagination
    search_fields = ['name', 'parent__name']
    filterset_class = CategoryFilter

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
