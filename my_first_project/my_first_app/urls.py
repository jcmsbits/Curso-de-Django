"""
URL configuration for my_first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from my_first_app.models import Profile, Author
from .views import my_class_view


def my_views(request, *arg, **args):
    author = Author.objects.filter(name = args['author'])
    profile = Profile.objects.filter(author_id = author[0].id)
    print('Profile: ',profile)   
    
    # HttpResponse("Biography:" + profile[0].biography + " Website: " + profile[0].website) 
    return HttpResponse(f"Biography {profile[0].biography} Website: {profile[0].website}") 








urlpatterns = [      
    path("listado", my_class_view.as_view()),
    path('author/<str:author>', my_views),
 
]