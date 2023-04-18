from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from crud.models import Person
from .forms import PersonForm, PersonModelForm


@login_required
def create_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)  # it runs validation
        if form.is_valid():
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            email = form.cleaned_data.get('email')
            department = form.cleaned_data.get('department')
            Person.objects.create(name=name, age=age, email=email, department=department)
            return redirect('home')
    context = {"form": PersonForm(), "title": "Create Person"}
    return render(request, "classbased/create_person.html", context)


def create_person_model_form(request):
    if request.method == "POST":
        form = PersonModelForm(request.POST)  # it runs validation
        if form.is_valid():
            form.save()
            # mail sending code
            return redirect('home')
    context = {"form": PersonModelForm(), "title": "Create Person Using Model Form"}
    return render(request, "classbased/create_person_model_form.html", context)


@method_decorator(login_required, name='dispatch')
class CreatePersonView(CreateView):
    model = Person
    template_name = "classbased/create_person_model_form.html"
    form_class = PersonModelForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title"] = "Create Person"
        return context


class PersonListView(ListView):
    # queryset = Person.objects.all()[:5]
    template_name = "classbased/person_list.html"
    context_object_name = "persons"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Person.objects.all()
        return Person.objects.all()[:5]


class PersonDetailView(DetailView):
    # model = Person
    queryset = Person.objects.all()
    template_name = "classbased/person_detail.html"
    pk_url_kwarg = 'id'
    context_object_name = "person"
