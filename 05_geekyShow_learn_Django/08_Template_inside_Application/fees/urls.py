from django.urls import path
from django.http import HttpResponse
from fees import views

urlpatterns = [
    path('feesdj/', views.fees_djnago),
    path('feespy/', views.fees_python),
]