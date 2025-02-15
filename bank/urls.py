"""
URL configuration for bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from atm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home ,name='home'),
    path('login/',views.login, name='login'),
    path('register/',views.register,name='register'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('create_account/',views.create,name='create_account'),
    path('deposit/',views.deposit,name='deposit'),
    path('withdraw/',views.withdrawal,name='withdraw'),
    path('check_balance/',views.check_balance,name='check_balance'),
    path('mini_statement/',views.mini_statement,name='mini_statement')
]
