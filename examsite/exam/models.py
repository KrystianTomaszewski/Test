from django.db import models
from django.urls import reverse
# Create your models here.

class Sheet(models.Model):
    sheet_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('exam:index', kwargs={'pk': self.pk})

    def __str__(self):
        return self.sheet_name

class Question(models.Model):
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('exam:question', kwargs={'pk': self.pk})

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('exam:choice', kwargs={'pk': self.pk})

    def __str__(self):
        return self.choice_text