from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    department=models.CharField(max_length=100)
    def __str__(self):
        return self.name
