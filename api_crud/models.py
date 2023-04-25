import uuid
from django.db import models


# This is an abstract class
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(TimeStampModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class ClassRoom(UUIDModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Person(UUIDModel):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE,
                                  related_name="classroom_people")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
