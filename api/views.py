import requests
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, \
    RetrieveUpdateDestroyAPIView

from crud.models import Person
from .serializers import PersonSerializer, PersonModelSerializer


def use_dummy_api(request):
    API_URL = "https://dummyjson.com/products/1"
    response = requests.get(API_URL)
    response = response.json()
    context = {"iphone": response}
    return render(request, 'api/dummy_api.html', context=context)


class HelloWorld(APIView):
    def get(self, *args, **kwargs):
        # response = {"message": "Hello World from rest framework"}
        people = [
            {
                "name": "Harry",
                "age": 24
            },
            {
                "name": "Jon",
                "age": 45
            }
        ]
        return Response(people)


class PersonView(APIView):
    def get(self, *args, **kwargs):
        name = self.request.GET.get("name")
        # name = request.GET.get("name")
        if name:
            persons = Person.objects.filter(name=name)
        else:
            persons = Person.objects.all()
        response = []
        for person in persons:
            response.append({
                "name": person.name,
                "age": person.age
            })
        return Response(response)
        # return Response({
        #     "name": person.name,
        #     "age": person.age,
        #     "email": person.email,
        #     "department": person.department
        # })


class PersonSerializedView(APIView):
    def get(self, *args, **kwargs):
        # person = Person.objects.get(id=2)
        person = Person.objects.all()  # this gives all person queryset
        # This step is not required if we use Serializer
        # response = {
        #     "name": person.name,
        #     "age": person.age
        # }
        # serializer = PersonSerializer(person)  # This is serialization
        serializer = PersonSerializer(person, many=True)  # This is serialization
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            email = serializer.validated_data.get('email')
            age = serializer.validated_data.get('age')
            department = serializer.validated_data.get('department')
            Person.objects.create(name=name, email=email, age=age, department=department)
            return Response({
                "message": "Person created successfully"
            }, status=status.HTTP_201_CREATED)
        return Response({
            "error": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class PersonModelSerializedView(APIView):
    def get(self, *args, **kwargs):
        person = Person.objects.all()

        # This is the process of serialization
        serializer = PersonModelSerializer(person, many=True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        serializer = PersonModelSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"msg": serializer.errors}, status=201)


class PersonListView(ListAPIView):
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class PersonListCreateView(ListCreateAPIView):
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class PersonRetrieveView(RetrieveAPIView):
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class PersonURDView(RetrieveUpdateDestroyAPIView):
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


# 200 => Get request Successful
# 201 => Post request Successful
# 204 => Delete successful

# 400 => Bad request / Client side error
# 401 => Unauthorized
# 403 => Forbidden
# 404 => Not Found
# 405 => Method not allowed


# 500 => Internal Server Error / Backend Error
# 502 => API Gateway error
