from django.db import models
from examsite.exam.models import Sheet
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10)
    Sheet = models.ManyToManyField(Sheet, blank=True)

    def __str__(self):
        return self.name
