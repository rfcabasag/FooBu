from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.foodHome, name="food-home"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
]