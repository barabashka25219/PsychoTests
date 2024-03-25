from django.shortcuts import render, redirect
from .forms import ProfileForm, UserCreationForm, UserLoginForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import Profile

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

            login(request, user)

            return redirect("polls:polls")
    
    return render(
            request, 
            "users/create.html", 
            context={
                "user_form": user_auth_form,
                "profile_form": user_profile_form
            }
        )

@require_http_methods(['GET', 'POST'])
def LoginUserView(request):
    if request.method == 'GET':
        login_form = UserLoginForm()
    
    else:
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('polls:polls')
            
    return render(
        request,
        'users/login.html',
        context={
            'login_form': login_form,
        }
    )

@require_http_methods(['GET', 'POST'])
@login_required
def ProfileView(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'GET':
        profile_form = ProfileForm(instance=profile)
    else:
        profile_form = ProfileForm(request.POST, instance=profile)
        
        if profile_form.is_valid():
            profile_form.save()
            
    return render(request, 'users/profile.html', context={
        'profile_form': profile_form,
    })

@require_http_methods(['GET'])
@login_required
def LogoutView(request):
    logout(request)
    return redirect('polls:polls')