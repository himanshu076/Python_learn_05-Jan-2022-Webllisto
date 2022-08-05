import imp
from django.shortcuts import render

# Create your views here.
def learn_djnago(request):
    return render(request, 'app/appone.html')

def learn_python(request):
    return render(request, 'app/apptwo.html')

