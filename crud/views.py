from django.shortcuts import render, redirect
from .models import Person


def home(request):
    context = {"persons": Person.objects.all(), "title": "Home"}
    return render(request, template_name="crud/person.html", context=context)


def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        department = request.POST.get("department")
        status = True if request.POST.get("status") else False
        Person.objects.create(name=name, email=email, age=age, department=department, is_active=status)
        return redirect("home")
    context = {"title": "Add Person"}
    return render(request, template_name="crud/add_person.html", context=context)


def update(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        department = request.POST.get("department")
        status = True if request.POST.get("status") else False
        Person.objects.filter(id=id).update(name=name,
                                            email=email,
                                            age=age,
                                            department=department,
                                            is_active=status)
        return redirect("home")
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return redirect('home')
    checked = "checked" if person.is_active else ""
    context = {"title": "Update Person", "person": person, "checked": checked}
    return render(request, "crud/update_person.html", context=context)


def delete(request, id):
    if request.method == "POST":
        Person.objects.filter(id=id).delete()
        return redirect("home")
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return redirect("home")
    context = {"title": "Delete Person", "person": person}
    return render(request, "crud/delete_person.html", context=context)