from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets


from Profile import views

urlpatterns = [
    re_path(r'profile/$', views.ProfileList.as_view()),
    re_path(r'profile/ciudad/$', views.CiudadList.as_view()),
    re_path(r'profile/genero/$', views.GeneroList.as_view()),
    re_path(r'profile/ocupacion/$', views.OcupacionList.as_view()),
    re_path(r'profile/estado/$', views.EstadoList.as_view()),
    re_path(r'profile/estadoCivil/$', views.EstadoCivilList.as_view()),

]