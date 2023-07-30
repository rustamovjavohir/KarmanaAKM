from django.urls import path

from api.books.views import CategoryListAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
]
