from django.urls import path
from . import views

app_name = 'exam'
urlpatterns = [
    path('<int:pk>/', views.SheetDetail.as_view(), name='sheet_detail'),
    path('<int:pk>/question', views.QuestionDetail.as_view(), name='question_detail'),
    path('<int:pk>/choice', views.ChoiceDetail.as_view(), name='choice_detail'),
]