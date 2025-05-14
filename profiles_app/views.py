from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import filters

from profiles_app import serializers
from profiles_app import models
from profiles_app import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles the view fro the User profile"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email")


class ProfileLoginApiView(ObtainAuthToken):
    """Handles the login and retrieving of authentication tokens"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class PostFeedViewSet(viewsets.ModelViewSet):
    """Creates the view for the post feed"""

    serializer_class = serializers.PostFeedSerializer
    queryset = models.PostFeed.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnPostFeed, IsAuthenticated)

    def perform_create(self, serializer):
        """sets the author to the logged in user"""
        serializer.save(author=self.request.user)
