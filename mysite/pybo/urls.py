from django.urls import path

from . import views

urlpatterns = [
    path('', views.ko1, name='ko1'),
    path('ko', views.ko, name='ko'),
    path('ko1', views.ko1, name='ko1'),
    path('survey', views.survey, name='survey'),

]