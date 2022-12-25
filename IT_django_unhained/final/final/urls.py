"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from database import views
urlpatterns = [
    path('', views.index),
    path('add_builder/', views.add_builder),
    path('add_building/', views.add_building),
    path('add_property_dev/', views.add_property_dev),
    path('show_builder/', views.show_builder),
    path('upload_builder/', views.upload_builder),
    path('download_builder_xml/', views.download_builder_xml),
]
