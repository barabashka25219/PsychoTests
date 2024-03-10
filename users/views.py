from django.shortcuts import render
from .forms import ProfileForm
from django.contrib.auth.forms import UserCreationForm

def create(request):
    if request.method == 'GET':
        user_auth_form = UserCreationForm()
        user_profile_form = ProfileForm()
        context = {
            "user_form": user_auth_form,
            "profile_form": user_profile_form
        }
        return render(request, "users/create.html", context)