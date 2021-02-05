from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_subscriptions, name='subscriptions'),
    path('<sub_id>', views.subscription_signup, name='subscription_signup'),
]
