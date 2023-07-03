from rest_framework import serializers
from src.personal.serializers import CustomUserSerializer
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('name', 'id')


class NestedProjectSerializer(serializers.ModelSerializer):
    employments = CustomUserSerializer(many=True, read_only=True)
    lead = CustomUserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('name', 'employments', 'lead', 'id')