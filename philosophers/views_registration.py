from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile, PhilosophySchool
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful. Welcome!')
            return redirect('philosophers:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    
    schools = PhilosophySchool.objects.all()
    
    if request.method == 'POST':
        # Handle profile updates
        favorite_school_id = request.POST.get('favorite_school')
        avatar_url = request.POST.get('avatar_url', '')
        
        if favorite_school_id:
            try:
                school = PhilosophySchool.objects.get(id=favorite_school_id)
                user_profile.favorite_school = school
            except PhilosophySchool.DoesNotExist:
                messages.error(request, 'Invalid philosophy school selected.')
        
        if avatar_url:
            user_profile.avatar_url = avatar_url
        
        user_profile.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('philosophers:profile')
    
    return render(request, 'registration/profile.html', {
        'profile': user_profile,
        'schools': schools
    })