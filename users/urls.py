from django.urls import path
from .views import CreateUserView, LoginUserView, ProfileView

app_name = 'users'

urlpatterns = [
    path('create/', CreateUserView, name="create_user"),
    path('login/', LoginUserView, name="login_user"),
    path('profile/', ProfileView, name="user_profile"),
]