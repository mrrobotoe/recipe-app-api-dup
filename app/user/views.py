"""
Views for the User API.
"""

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""

    serializer_class = AuthTokenSerializer
    # gui view on web
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authentication user."""

    serializer_class = UserSerializer
    # how do you know if the user is the user
    authentication_classes = [authentication.TokenAuthentication]
    # we know who you are what is it that they are allowed to do
    # must be authenticated to use this api
    permission_classes = [permissions.IsAuthenticated]

    # override  retrieving the user the request.
    # gets assigned the user to the request object
    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
