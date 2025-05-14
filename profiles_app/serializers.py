from rest_framework import serializers
from profiles_app import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes the profiles api"""

    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def create(self, validated_data):
        """Creates the UserProfile"""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        """Handles updating a user profile password"""
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)


class PostFeedSerializer(serializers.ModelSerializer):
    """Serializes the post feed"""

    class Meta:
        model = models.PostFeed
        fields = ("id", "author", "title", "content", "date_created")
        extra_kwargs = {"author": {"read_only": True}}
