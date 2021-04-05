"""CRM_Automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import *
from django.shortcuts import render

urlpatterns = [
    path("",lambda request:render(request,"crmapp/ch_base.html")),
    path('course',Course_Registration.as_view(),name='course'),
    path('course_edit/<int:id>',Course_edit.as_view(),name="course_edit"),
    path('course_delete/<int:id>',Course_delete.as_view(),name="course_delete"),
    path('batch', Batch_Creation.as_view(), name='batch'),
    path('batch_edit/<int:id>', Batch_edit.as_view(), name='batch_edit'),
    path('batch_delete/<int:id>', Batch_delete.as_view(), name='batch_delete'),

]
