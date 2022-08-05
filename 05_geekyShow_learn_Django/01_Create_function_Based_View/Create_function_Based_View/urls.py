"""Create_function_Based_View URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

'''
Syntex : URL Dispatcher
        urlpatterns = [
            path(route, views, kwargs=None, name=None)
        ]

        urlpatterns = [
            path('learndj/, views.learn_django, {'check' : 'Ok'},name='learn_django')
        ]

        where,
            The route argument should be a string or gettext_lazy() that contains a URL pattern. the string may contain angle brackets e.g. <username> to capture part of the URL and sent it as a keyword arguments to the view. The angle brackets may include a convertor specification like the int part of <int:id> which limits the characters matched and may also changed the type of the variable passed to the view. For Example, <int:id> matches the string of decimal degits and convert the value to an int.
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('learndj/', views.learn_django),
    path('learnpy/', views.learn_python),
    path('learnv/', views.learn_var),
    path('learnm/', views.learn_math),
    path('learnf/', views.learn_format),
]
