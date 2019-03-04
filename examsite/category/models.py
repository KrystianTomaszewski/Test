from django.db import models
from exam.models import Sheet
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10)
    Sheet = models.ManyToManyField(Sheet, blank=True)

    def __str__(self):
        return self.name
