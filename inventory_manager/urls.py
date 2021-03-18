"""inventory URL Configuration

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
from django.contrib import admin
from django.urls import path
from .views import (
home,
add_item,
purchases,
show,
find_item,
sales,
addtocart,
place_order,
logout,
deletecartitem
)


urlpatterns = [
    path('',home,name="home" ),
    path('show',show,name="show"),
    path('sale',sales,name="sale"),
    path('logout',logout,name="logout"),
    path('addtocart/<slug>',addtocart,name="addtocart"),
    path('deletecartitem/<slug>',deletecartitem,name="deletecartitem"),
    path('place_order',place_order,name="place_order"),
    path('find_item',find_item,name="find_item"),
    path('add_item',add_item,name="add_item"),
    path('purchase',purchases,name="purchase"),
]
