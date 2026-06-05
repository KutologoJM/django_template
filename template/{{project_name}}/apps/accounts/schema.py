from drf_spectacular.extensions import OpenApiAuthenticationExtension
from knox.auth import TokenAuthentication


class KnoxTokenScheme(OpenApiAuthenticationExtension):
    target_class = TokenAuthentication
    name = 'knoxTokenAuth'

    def get_security_definition(self, auto_schema):
        return {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization',
            'description': 'Token-based authentication. Format: "Token <your_knox_token>"'
        }
