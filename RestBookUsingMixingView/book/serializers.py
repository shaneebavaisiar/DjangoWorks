from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Book

class BookSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()

