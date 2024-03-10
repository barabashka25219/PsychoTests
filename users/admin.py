from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile

class AdminProfile(admin.ModelAdmin):
    list_display = ['user', 'sex', 'birth_date', 'bio']

admin.site.register(Profile, AdminProfile)