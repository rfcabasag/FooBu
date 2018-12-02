from django.contrib import admin
from .models import RegisteredUser, Establishment, FoodItem, Rates, Favorites

admin.site.register(RegisteredUser)
admin.site.register(Establishment)
admin.site.register(FoodItem)
admin.site.register(Rates)
admin.site.register(Favorites)
