from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('slides', views.all_slides, name="slides"),
    path('add/', views.add_slide, name='add_slide'),
    path('edit/<int:slide_id>/', views.edit_slide, name='edit_slide'),
    path('delete/<int:slide_id>/', views.delete_slide, name='delete_slide'),
]
