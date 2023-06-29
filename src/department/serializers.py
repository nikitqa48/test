from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('name', 'director', 'personal')


class DepartmentPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('personal', 'name')
        extra_kwargs = {
            'name': {'required': True},
            'personal': {'required': True},
        }

    def create(self, validated_data):
        instance = Department.objects.get(name=validated_data['name'])
        for persona in validated_data['personal']:
            instance.personal.add(persona)
        return instance



