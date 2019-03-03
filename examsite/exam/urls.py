from django.urls import path
from . import views

app_name = 'exam'
urlpatterns = [
    path('', views.SheetList.as_view(), name='index'),
    path('<int:pk>/question', views.QuestionList.as_view(), name='question'),
    path('<int:pk>/choice', views.ChoiceList.as_view(), name='choice'),
    path('<int:pk>/', views.SheetDetail.as_view(), name='detail')
]