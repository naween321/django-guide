from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from .models import Student, Experience


def home(request):
    context = {
        "experiences": Experience.objects.all()
    }
    return render(request, template_name="myapp/index.html", context=context)


def name_func(request, name):
    data = {
        "ram": "Ram Bahadur",
        "hari": "Hari Krishna"
    }
    name = data.get(name)
    if not name:
        return HttpResponseNotFound("<h1>Invalid URL</h1>")
    return HttpResponse(f"<h1>Hello I am {name}</h1>")


def template(request):
    # Context should always be a dictionary
    context = {"name": "Jon Snow", "age": 25, "hobbies": ["sports", "movies", "reading"]}
    # template = loader.get_template("myapp/home.html")
    # template_data = template.render(context, request)
    # return HttpResponse(template_data)
    return render(request, template_name="myapp/home2.html", context=context)


def inside_template(request):
    return render(request, template_name="myapp/inside_home.html")


def about(request):
    return render(request, template_name="myapp/about.html")


def students(request):
    try:
        student = Student.objects.get(id=3)
    except:
        pass
    # context = {"name": student.name, "age": student.age,
    #            "department": student.department}
    context = {
        "infos": Student.objects.all()
    }
    return render(request, "myapp/students.html", context)


# MVT
# M => Model
# V => Views
# T => Template
