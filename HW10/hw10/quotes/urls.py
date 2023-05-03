from django.urls import path

from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='users'),
    path('<int:page>', views.main, name='root_paginate'),
    path('add_quotes/', views.add_quotes, name='add_quotes'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_tag/', views.add_tag, name='add_tag')
]