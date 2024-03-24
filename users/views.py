from django.shortcuts import render, redirect
from .forms import ProfileForm, UserCreationForm
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def CreateUserView(request):

    if request.method == 'GET':
        user_auth_form = UserCreationForm()
        user_profile_form = ProfileForm()
    
    else:
        user_auth_form = UserCreationForm(request.POST)
        user_profile_form = ProfileForm(request.POST)

        if user_auth_form.is_valid() and user_profile_form.is_valid():
            user = user_auth_form.save()
            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user
            user_profile.save()

            return redirect("polls:polls")
    
    return render(
            request, 
            "users/create.html", 
            context={
                "user_form": user_auth_form,
                "profile_form": user_profile_form
            }
        )