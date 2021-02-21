from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscriptions, name='subscriptions'),
    path('add/', views.add_subscription, name='add_subscription'),
]
