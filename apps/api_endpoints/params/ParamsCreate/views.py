from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.api_endpoints.params.ParamsCreate.serializers import ParamsCreateSerializer
from apps.api_endpoints.params.ParamsCreate.service.predict import predict_label
from apps.models import Params
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

class ParamsListCreateView(ListCreateAPIView):
    queryset = Params.objects.all()
    serializer_class = ParamsCreateSerializer

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'x2': openapi.Schema(type=openapi.TYPE_NUMBER),
                'x6': openapi.Schema(type=openapi.TYPE_NUMBER),
                'x11': openapi.Schema(type=openapi.TYPE_NUMBER),
                'x12': openapi.Schema(type=openapi.TYPE_NUMBER),
                'x18': openapi.Schema(type=openapi.TYPE_NUMBER),
                'x19': openapi.Schema(type=openapi.TYPE_NUMBER),
            }
        ),
        responses={status.HTTP_200_OK: openapi.Response(description='Success')}
    )
    def post(self, request):
        serializer = ParamsCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params_data = serializer.validated_data
        response_data = predict_label(params_data)
        return Response(data=response_data, status=status.HTTP_200_OK)
