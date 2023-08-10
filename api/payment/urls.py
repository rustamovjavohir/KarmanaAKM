from django.urls import path

from api.payment.views import CardCreateApiView

urlpatterns = [
    path('create-card/', CardCreateApiView.as_view(), name='create-card'),
]
