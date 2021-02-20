from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name="signup"),
    path('<sub_id>/', views.signup, name="signup"),
    path('payment_success/<order_number>', views.payment_success, name="payment_success"),
]
