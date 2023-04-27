from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny

from .viewsets import ListCreateUpdateDestroyViewSet, CreateUpdateDestroyViewSet, ListUpdateDestroyViewSet
from .models import ClassRoom, Person, PersonProfile
from .permissions import IsSuperAdminUser, IsAdminUser
from .serializers import ClassRoomSerializer, PersonSerializer, \
    PersonProfileSerializer, UserSerializer
"""
Get, Post, Put, Patch, Delete, Options, Head  => These are HTTP Methods
List, Retrieve, Create, Update, Partial Update, Destroy => Actions (Django Specific)
"""


class ClassRoomViewSet(ListCreateUpdateDestroyViewSet):
    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"
    # serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()

    def get_serializer_class(self):
        if self.action == 'person':
            return PersonSerializer
        return ClassRoomSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny(), ]
        # api/crud/classroom/{uuuid}/  delete
        if self.action in ['create', 'destroy']:
            return [(IsAdminUser | IsSuperAdminUser)()]
        if self.action in ['update', 'people', "partial_update"]:
            return [IsAuthenticated()]

    @action(detail=True)
    def people(self, *args, **kwargs):
        classroom_obj = self.get_object()
        person = Person.objects.filter(classroom=classroom_obj)
        serializer = self.get_serializer(person, many=True)
        return Response(serializer.data)

    # 127.0.0.1:8000/api/crud/classroom/{uuid}/person/
    # 127.0.0.1:8000/api/crud/classroom/{uuid}/teachers/


class PersonViewSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    lookup_field = 'uuid'
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    def get_serializer_class(self):
        if self.action == 'profile':
            return PersonProfileSerializer
        return PersonSerializer

    @action(detail=True)
    def profile(self, *args, **kwargs):
        person = self.get_object()
        try:
            p_profile = person.person_profile  # Here person_profile is a related-name
        except:
            return Response({
                "message": "Profile for this person doesn't exist"
            })
        serializer = self.get_serializer(p_profile)
        return Response(serializer.data)


class ClassRoomPersonView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        classroom_uuid = self.kwargs['uuid']
        return Person.objects.filter(classroom__uuid=classroom_uuid)


class PersonProfileViewSet(CreateUpdateDestroyViewSet):
    lookup_field = 'uuid'
    lookup_url_kwarg = 'uuid'
    serializer_class = PersonProfileSerializer
    queryset = PersonProfile.objects.all()


class UserViewSet(ListUpdateDestroyViewSet):
    permission_classes = [AllowAny, ]
    lookup_field = "username"
    lookup_url_kwarg = "username"
    serializer_class = UserSerializer
    queryset = User.objects.all()

# person/uuid/profile/
