from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    name = "하정민"
    age = "25"
    hobby = "baseball"
    return render(request, 'index.html', {"my_name" : name, "my_age" : age, "my_hobby" : hobby})