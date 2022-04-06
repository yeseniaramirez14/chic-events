from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=50)
    members = models.ManyToManyField(USER_MODEL, related_name="events")

    def __str__(self):
        return self.name

class Description(models.Model):
    description_list = models.CharField(max_length=200)
    event = models.ForeignKey (
        "Event",
        related_name = "description_list",
        on_delete = models.CASCADE
    )

    def __str__(self):
        return f'{self.description_list} for {self.event}'

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'From {self.first_name}: {self.email}'
