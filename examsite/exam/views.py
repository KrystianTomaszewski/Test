from django.shortcuts import render
from django.views import generic
from .models import Sheet, Question, Choice




# Create your views here.

class SheetList(generic.ListView):
    model = Sheet

    def __str__(self):
        return self.Sheet.name

sheet_list = SheetList.as_view()

class QuestionList(generic.ListView):
    model = Question

    def __str__(self):
        return self.Question.name

question_list = QuestionList.as_view()

class ChoiceList(generic.ListView):
    model = Choice

    def __str__(self):
        return self.Choice.name

choice_list = ChoiceList.as_view()

