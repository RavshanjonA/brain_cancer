from rest_framework.generics import ListCreateAPIView

from apps.api_endpoints.users.UserCreate.serializers import UserCreateSerializer
from apps.models import Users


class UserCreateView(ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserCreateSerializer


