from rest_framework import serializers
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User 

from .models import Profile, Post, LikePost, FollowersCount

#User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            "id",
            "username",
        ]

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "user", 
            "id_user",
            "bio",
            "profileimg",
            "location",
        ]



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "image",
            "caption",
            "created_at",
            "no_of_likes",
        ]

class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikePost
        fields = [
            "post_id",
            "username",
        ]

class FollowersCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowersCount
        fields = [
            "follower",
            "user",
        ]