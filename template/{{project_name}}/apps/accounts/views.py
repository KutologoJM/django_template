from drf_spectacular.openapi import AutoSchema as SpectacularAutoSchema
from drf_spectacular.utils import extend_schema
from knox.views import (
    LoginView as KnoxLoginView,
    LogoutView as KnoxLogoutView,
    LogoutAllView as KnoxLogoutAllView,
)
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer


# Defines what Knox actually returns on a successful login
class KnoxLoginResponseSerializer(serializers.Serializer):
    token = serializers.CharField(help_text="The secure token string to place in your Authorization header.")
    expiry = serializers.DateTimeField(help_text="The timestamp when this token expires.")


class LoginView(KnoxLoginView):
    schema = SpectacularAutoSchema()

    @extend_schema(
        request=AuthTokenSerializer,
        responses={200: KnoxLoginResponseSerializer},
        auth=[],
        description="Submit credentials to receive a fresh Knox authentication token."
    )
    def post(self, request, format=None):
        return super().post(request, format)


class LogoutView(KnoxLogoutView):
    schema = SpectacularAutoSchema()

    @extend_schema(
        request=None,
        responses={204: None},
        description="Invalidate and delete the token used for the current session."
    )
    def post(self, request, format=None):
        return super().post(request, format)


class LogoutAllView(KnoxLogoutAllView):
    schema = SpectacularAutoSchema()

    @extend_schema(
        request=None,
        responses={204: None},
        description="Invalidate and delete every active token associated with this account."
    )
    def post(self, request, format=None):
        return super().post(request, format)
