from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('list',views.targetHeight,name='detail'),
    path('player/',views.PlayerView.as_view(),name='Player')
]