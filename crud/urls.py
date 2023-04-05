from django.urls import path
from .views import home, create, update, delete, file_test


urlpatterns = [
    path("create/", create, name="create"),
    path("file-test/", file_test, name="file_test"),
    path("update/<int:id>/", update, name="update"),
    path("delete/<int:id>/", delete, name="delete"),
    path("", home, name='home'),
]