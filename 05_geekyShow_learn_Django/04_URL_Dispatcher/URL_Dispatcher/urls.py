"""URL_Dispatcher URL Configuration

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

'''
Include Syntex :
        include(module, namespace=None)
        include(pattern_list)
        include((pattern_list, app_namespace), namespace=None)
        where,
            module - URLconf module (or module name)
            namespace(str) - Instance namespace fro the URL entries being included
            pattern_list - Iterable of path() and/or re_path() instances.
            app_namespace(str) - Application namespace for the URLentries being included
'''

from django.contrib import admin
from django.urls import path, include
from app import views as ap
from fees import views as fe

'''Method 1 to define include URl: '''
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('app/', include('app.urls')),
#     path('fe/', include('fees.urls')),
# ]


'''Method 2 to define include URl: '''

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('app/', include([
#         path('learndj/', ap.learn_djnago),
#         path('learnpy/', ap.learn_python),
#     ])),

#     path('fe/', include([
#         path('feesdj/', fe.fees_djnago),
#         path('feespy/', fe.fees_python),
#     ])),
# ]


'''Method 3 to define include URl: '''

appPattern = [
        path('learndj/', ap.learn_djnago),
        path('learnpy/', ap.learn_python),
    ]

feePattern = [
        path('feesdj/', fe.fees_djnago),
        path('feespy/', fe.fees_python),
    ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include(appPattern)),
    path('fe/', include(feePattern)),
]