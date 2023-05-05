from django.db import models


class ClassRoom(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    # group = models.ManyToManyField(Group, related_name="group_person")

    def __str__(self):
        return self.name

    @property
    def birth_year(self):
        year = 2023 - self.age
        return year


class PersonGroup(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='person_group')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="group_person")
    date_added = models.DateTimeField(auto_now_add=True)

class PersonProfile(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE,
                                  related_name="person_profile")
    profile_picture = models.FileField(upload_to="profile_picture", null=True, blank=True)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE,
                                  related_name="classroom_people")


class FileStorage(models.Model):
    file = models.FileField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
