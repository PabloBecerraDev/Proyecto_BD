from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.



class IndexTemplate(TemplateView):
    template_name = "home/index.html"
