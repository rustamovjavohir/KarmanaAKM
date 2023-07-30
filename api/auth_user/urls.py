from django.urls import path

from api.auth_user.views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='users'),
]
