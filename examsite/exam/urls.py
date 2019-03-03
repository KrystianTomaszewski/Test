from django.urls import path
from . import views

app_name = 'exam'
urlpatterns = [
    path('<int:pk>/', views.SheetList.as_view(), name='index'),
    path('<int:pk>/question', views.QuestionList.as_view(), name='question'),
    path('<int:pk>/question:choice', views.ChoiceList.as_view(), name='choice'),
]