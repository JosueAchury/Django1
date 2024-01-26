from django.contrib import admin
from django.urls import path
from . import views
from myproject.views import *



urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/login', login_view, name='login'),
    path('usuarios/logout', views.logout_view, name='logout'),
    path('usuarios/registro', views.registro, name='registro'),
    path('registro/', views.resgistro1, name='registro1'),
    path('admin/', admin.site.urls),
]
