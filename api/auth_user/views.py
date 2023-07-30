from rest_framework.permissions import AllowAny

from api.auth_user.serializers import UserSerializer
from apps.auth_user.models import User
from rest_framework.generics import ListAPIView


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    # pagination_class = UserPagination
    # filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
