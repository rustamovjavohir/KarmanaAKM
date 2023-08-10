from django.urls import path, include
from apps.views import IndexView
from api.events.urls import urlpatterns as events_urls
from api.auth_user.urls import urlpatterns as auth_user_urls
from api.books.urls import urlpatterns as books_urls
from api.payment.urls import urlpatterns as payment_urls

urlpatterns = [
    path('event/', include(events_urls)),
    path('auth/', include(auth_user_urls)),
    path('books/', include(books_urls)),
    path('payment/', include(payment_urls)),
]
