from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Person, FileStorage, ClassRoom, PersonProfile


@login_required
def home(request):
    context = {"persons": Person.objects.all(), "title": "Home"}
    return render(request, template_name="crud/person.html", context=context)


@login_required
def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        department = request.POST.get("department")
        status = True if request.POST.get("status") else False
        bio = request.POST.get("bio")
        profile_picture = request.FILES.get("pp")
        address = request.POST.get("address")
        classroom = request.POST.get("classroom")
        c = ClassRoom.objects.get(name=classroom)
        p = Person.objects.create(name=name, email=email, age=age, department=department, is_active=status)
        PersonProfile.objects.create(bio=bio, address=address, profile_picture=profile_picture, person=p,
                                     classroom=c)
        return redirect("home")
    context = {"title": "Add Person", "classrooms": ClassRoom.objects.all()}
    return render(request, template_name="crud/add_person.html", context=context)


@login_required
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


@login_required
def delete(request, id):
    if request.method.lower() == "post":
        Person.objects.filter(id=id).delete()
        return redirect("home")
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        return redirect("home")
    context = {"title": "Delete Person", "person": person}
    return render(request, "crud/delete_person.html", context=context)


@login_required
def file_test(request):
    if request.method == "POST":
        file = request.FILES.get("uploaded_file")
        FileStorage.objects.create(file=file, name=file.name)
        return redirect('file_test')
    context = {"infos": FileStorage.objects.all()}
    return render(request, "crud/file_test.html", context)


@login_required
def classroom(request):
    context = {"title": "Classrooms", "classrooms": ClassRoom.objects.all()}
    return render(request, "crud/classroom.html", context=context)


@login_required
def add_classroom(request):
    if request.method == "POST":
        name = request.POST.get('classroom')
        ClassRoom.objects.create(name=name)
        return redirect("classroom")
    context = {"title": "Add Classroom"}
    return render(request, "crud/add_classroom.html", context)


@login_required
def person_detail(request, id):
    try:
        person_profile = PersonProfile.objects.get(person_id=id)
    except PersonProfile.DoesNotExist:
        person_profile = None
    context = {"title": f"Detail View",
               "person_profile": person_profile}
    return render(request, "crud/detail_person.html", context=context)
