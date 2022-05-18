from django.contrib import admin
from .models import UserProfile, State, City, College

admin.site.register(UserProfile)
admin.site.register(State)
admin.site.register(City)
admin.site.register(College)
