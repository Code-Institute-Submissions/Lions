from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscriptions, name='subscriptions'),
    path('categories/', views.all_categories, name='categories'),
    path('add/', views.add_subscription, name='add_subscription'),
    path('edit/<int:subscription_id>/', views.edit_subscription, name='edit_subscription'),
    path('delete/<int:subscription_id>/', views.delete_subscription, name='delete_subscription'),
    path('add_category/', views.add_category, name='add_category'),
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
]
