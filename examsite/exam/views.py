from django.views import generic
from .models import Sheet, Question, Choice



# Create your views here.


class SheetDetail(generic.DetailView):
    model = Sheet
    template_name = 'exam/sheet_detail.html'

sheet_detail = SheetDetail.as_view()

class QuestionDetail(generic.DetailView):
    model = Question
    template_name = 'exam/question_detail.html'


question_detail= QuestionDetail.as_view()


class ChoiceDetail(generic.DetailView):
    model = Choice
    template_name = 'exam/choice_detail.html'

choice_detail = ChoiceDetail.as_view()

