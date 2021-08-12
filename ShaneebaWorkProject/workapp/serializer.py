from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *


class WorkSerializer(ModelSerializer):
    class Meta:
        model=Works
        fields="__all__"