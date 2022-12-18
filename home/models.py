from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=1000)
    age = models.IntegerField()

    def __str__(self):
        return self.name