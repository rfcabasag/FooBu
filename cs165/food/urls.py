from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.foodHome, name="food-home"),
    path('signup-as/', views.signup_as, name='signup-as'),
    path('register-owner/', views.register_as_owner, name="register-owner"),
    path('register-customer/', views.register_as_customer, name="register-customer"),
    path('fav-<int:est_id>/', views.favorite, name="favorite"),
    path('profile/', views.profile, name="profile"),
    path('profile/addestablishment', views.addestablishment, name="addestablishment"),
    path('profile/updateestablishment-<int:est_id>/', views.updateestablishment, name="updateestablishment"),
    path('profile/deleteestablishment-<int:est_id>/', views.deleteestablishment, name="deleteestablishment"),
    path('est-<int:est_id>/', views.establishment, name="establishment"),
    path('est-<int:est_id>/addfooditem/', views.addfooditem, name="addfooditem"),
    path('est-<int:est_id>/updatefooditem-<int:food_id>/', views.updatefooditem, name="updatefooditem"),
    path('est-<int:est_id>/deletefooditem-<int:food_id>/', views.deletefooditem, name="deletefooditem"), 
    path('est-<int:est_id>/addrating/', views.addrating, name="addrating"), 
    path('est-<int:est_id>/updaterating/', views.updaterating, name="updaterating"), 
    path('est-<int:est_id>/deleterating/', views.deleterating, name="deleterating"), 
]