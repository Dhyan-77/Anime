from rest_framework import serializers
from .models import Animemodel
from django.contrib.auth.models import User


class Animemodelserial(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Animemodel
        fields = ["id", "title", "description", "photos", "created_at", "username"]


class Signupserializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "password","email"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email =validated_data["email"]
        )
        return user
