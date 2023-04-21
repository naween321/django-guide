from rest_framework import serializers
from crud.models import Person, ClassRoom, PersonProfile


# Serializer does serialization and deserialization
class PersonSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    age = serializers.IntegerField()
    department = serializers.CharField()


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name", "age", "email", "department"]


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"


class PersonProfileSerializer(serializers.ModelSerializer):
    classroom = ClassRoomSerializer()
    person = PersonSerializer()

    class Meta:
        model = PersonProfile
        fields = ["id", "profile_picture", "bio", "address", "person", "classroom"]
