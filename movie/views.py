from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to home Page</h1>')
    #return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'Paola Vallejo'})


def about(request):
    return HttpResponse('<h1>Welcome to About page</h1>')