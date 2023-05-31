from rest_framework.serializers import ModelSerializer

from apps.models import Users, Params


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = (
            'id',
            'first_name',
            'last_name',
            'age',
            'region',
            'district',
        )

