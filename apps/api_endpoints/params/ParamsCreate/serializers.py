from rest_framework.serializers import ModelSerializer

from apps.models import Params


class ParamsCreateSerializer(ModelSerializer):
    class Meta:
        model = Params
        fields = (
            'x2',
            'x6',
            'x11',
            'x12',
            'x18',
            'x19',
        )