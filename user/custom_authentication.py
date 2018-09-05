from rest_framework.authentication import BaseAuthentication, get_authorization_header
import jwt, json
from rest_framework import status, exceptions
from rest_framework.response import Response

from user.models import User


class TokenAuthentication(BaseAuthentication):
    model = None

    def authenticate(self, request):
        auth = get_authorization_header(request).split()
        if len(auth) == 1:
            msg = 'Invalid token header. No credentials provided.'
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = 'Invalid token header'
            raise exceptions.AuthenticationFailed(msg)

        try:
            token = auth[1]
            if token == "null":
                msg = 'Null token not allowed'
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = 'Invalid token header. Token string should not contain invalid characters.'
            raise exceptions.AuthenticationFailed(msg)

        return self.authenticate_credentials(token)

    def get_model(self):
        return User

    def authenticate_credentials(self, token):
        model = self.get_model()
        payload = jwt.decode(token, "SECRET_KEY")
        try:
            user = model.objects.get(**payload)
        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return Response({'Error': "Token is invalid"}, status=403)
        except User.DoesNotExist:
            return Response({'Error': "Internal server error"}, status=500)

        return (user, token)

    def authenticate_header(self, request):
        return 'Token'
