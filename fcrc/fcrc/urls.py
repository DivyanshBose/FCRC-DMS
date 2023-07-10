"""
URL configuration for fcrc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from dms.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registration/', registration, name='registration'),
    path('emp_login/',emp_login, name='emp_login'),
    path('emp_home/',emp_home, name='emp_home'),
    path('logout/',Logout, name='logout'),
    path('admin_login/',admin_login, name='admin_login'),
    path('addComponent/',addComponent, name='addComponent'),
    path('viewComponent/',viewComponent, name='viewComponent'),
    path('admin_home/',admin_home, name='admin_home'),
    path('all_components/',all_components, name='all_components'),
    path('admin_addComponent/',admin_addComponent, name='admin_addComponent'),
    path('delete_component/<int:pid>',delete_component, name='delete_component'),
    path('edit_component/<int:pid>',edit_component, name='edit_component'),
   

    path('', include('django_dyn_dt.urls')),
]

