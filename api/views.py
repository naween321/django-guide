import requests
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from crud.models import Person


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
    def get(self, request, *args, **kwargs):
        persons = Person.objects.all()[:3]
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
