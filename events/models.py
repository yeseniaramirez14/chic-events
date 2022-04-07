from django.db import models
from django.conf import settings

USER_MODEL = settings.AUTH_USER_MODEL


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    price = models.CharField(max_length=50)

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

class BookRequest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    phone_number = models.CharField(max_length=20)
    guests = models.PositiveSmallIntegerField()
    description = models.TextField()
    package = models.ForeignKey(
        "Event",
        related_name = "package_type",
        on_delete = models.PROTECT
    )

    def __str__(self):
        return f'Request from {self.first_name} for {self.date}'
