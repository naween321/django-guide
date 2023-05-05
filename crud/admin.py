from django.contrib import admin
from .models import Person, Group, PersonGroup

admin.site.register(Person)
admin.site.register(Group)
admin.site.register(PersonGroup)
