from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.foodHome, name="food-home"),
    path('signup-as/', views.signup_as, name='signup-as'),
    path('register-owner/', views.register_as_owner, name="register-owner"),
    path('register-customer/', views.register_as_customer, name="register-customer"),
    path('profile/', views.profile, name="profile"),
    path('est-<int:est_id>/', views.establishment, name="establishment"),
    path('est-<int:est_id>/addfooditem/', views.addfooditem, name="addfooditem")
]