from django.urls import path
from . import views

app_name = 'category'
urlpatterns = [
    path('', views.CategoryList.as_view(), name='category'),
]