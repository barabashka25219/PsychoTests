from django.urls import path, include
from .views import CreateUserView

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('create/', CreateUserView, name="create_user"),
]