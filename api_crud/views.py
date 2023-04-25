from rest_framework.viewsets import ModelViewSet
from .viewsets import ListCreateUpdateDestroyViewSet
from .models import ClassRoom, Person
from .serializers import ClassRoomSerializer, PersonSerializer
"""
Get, Post, Put, Patch, Delete, Options, Head  => These are HTTP Methods
List, Retrieve, Create, Update, Partial Update, Destroy => Actions (Django Specific)
"""


class ClassRoomViewSet(ListCreateUpdateDestroyViewSet):
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()


class PersonViewSet(ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
