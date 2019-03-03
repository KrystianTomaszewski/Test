from django.shortcuts import render
from django.views import generic
from .models import Category

# Create your views here.

class CategoryList(generic.ListView):
    model = Category
    template_name = 'category/category.html'

    def __str__(self):
        return self.Category.name

category_list = CategoryList.as_view()

