from django.shortcuts import render
from django.http import HttpResponse


# Create your views heres.
def index(request):
    context = {
        'name' : 'Paxil',
        'age' : 90,
        'nationality' : 'indian',
    }
    return render(request ,'index.html' , context)