from rest_framework import serializers
from .models import ClassRoom, Person


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ['uuid', 'created_at', 'updated_at', 'name']


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        read_only_fields = ['uuid', 'created_at', 'updated_at']
        fields = read_only_fields + ["name", "email", "age", "classroom", "is_active"]
