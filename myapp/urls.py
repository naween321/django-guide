from django.urls import path
from .views import home, name_func, template, inside_template, students, about   # Relative import

urlpatterns = [
    path('template/', template, name='template'),
    path('inside-template/', inside_template, name="inside_template"),
    path('students/', students, name="students"),
    path('about/', about, name="about"),
    # path("<str:name>/", name_func),
    path("", home, name='home')
]
