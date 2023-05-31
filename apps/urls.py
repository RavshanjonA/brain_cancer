from django.urls import path

from apps.api_endpoints.params.ParamsCreate.views import ParamsListCreateView
from apps.api_endpoints.users.UserCreate.views import UserCreateView


urlpatterns = [
    path('users', UserCreateView.as_view(), name='users'),
    path('params', ParamsListCreateView.as_view(), name='params'),
]
