from django.shortcuts import render
from django.views import generic
from .models import Sheet, Question, Choice
from django.template import loader




# Create your views here.

class SheetList(generic.ListView):
    model = Sheet
    template_name = 'exam/index.html'

    def __str__(self):
        return self.Sheet.name

sheet_list = SheetList.as_view()

class QuestionList(generic.ListView):
    model = Question
    template_name = 'exam/question.html'

    def __str__(self):
        return self.Question.name

question_list = QuestionList.as_view()

class ChoiceList(generic.ListView):
    model = Choice
    template_name = 'exam/question/choice.html'

    def __str__(self):
        return self.Choice.name

choice_list = ChoiceList.as_view()

class SheetDetail(generic.DetailView):
    model = Sheet
    template_name = 'exam/index.html'


sheet_detail = SheetDetail.as_view()

class QuestionDetail(generic.DetailView):
    model = Question
    template_name = 'exam/question.html'

question_detail= QuestionDetail.as_view()

