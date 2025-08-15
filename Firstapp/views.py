from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.
# class Myviewclass(View):
#     def get(self,request):
#         return HttpResponse("<h1>This Professor<h1>")

    
class myclassview(TemplateView):
    template_name = "index.html"
    