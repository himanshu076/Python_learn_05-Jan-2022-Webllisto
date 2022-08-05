from django.urls import path
from django.http import HttpResponse
from app import views

urlpatterns = [
    path('learndj/', views.learn_djnago),
    path('learnpy/', views.learn_python),
]