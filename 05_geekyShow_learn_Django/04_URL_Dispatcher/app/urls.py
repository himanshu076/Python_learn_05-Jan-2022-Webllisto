from django.urls import path
from app import views

urlpatterns = [
    path('learndj/', views.learn_djnago),
    path('learnpy/', views.learn_python),
]
