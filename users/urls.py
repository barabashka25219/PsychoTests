from django.urls import path
from .views import create

app_name = 'users'

urlpatterns = [
    path('create', create, name="create"),
]