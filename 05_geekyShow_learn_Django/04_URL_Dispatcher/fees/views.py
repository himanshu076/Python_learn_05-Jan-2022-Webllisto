import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_djnago(request):
    return HttpResponse('3000')

def fees_python(request):
    return HttpResponse('200')