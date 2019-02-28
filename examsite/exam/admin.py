from django.contrib import admin

# Register your models here.
from .models import Sheet, Question, Choice
admin.site.register(Sheet)
admin.site.register(Question)
admin.site.register(Choice)