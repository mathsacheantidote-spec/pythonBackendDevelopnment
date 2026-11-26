from django.shortcuts import render
from django.http import HttpResponse


# Create your views heres.
def index(request):
    return render(request ,'index.html')