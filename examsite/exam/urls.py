from django.urls import path
from . import views

app_name = 'exam'
urlpatterns = [
    path('', views.SheetList.as_view(), name='sheetlist'),
    path('question', views.QuestionList.as_view(), name='questionlist'),
    path('choice', views.ChoiceList.as_view(), name='choicelist'),
]