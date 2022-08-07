"""s1 URL Configuration

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
from s1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('index/',views.index),
    path('portfolio/',views.porfolio),
    path('contant/',views.contant),
    path('post/',views.post),
    path('submit/',views.submit,name='sub'),
    path('security/',views.security,name='secu'),
    path('calcu/',views.calcu,name="cal"),
    path('marks/',views.marksheet,name="mar"),
    path('ev$od/',views.ev_od),
    path('news/<newid>',views.newsdetail)
]
