from django.urls import path, include
from .views import CreateUserView, LoginUserView

app_name = 'users'

urlpatterns = [
    path('create/', CreateUserView, name="create_user"),
    path('login/', LoginUserView, name="login_user"),
]