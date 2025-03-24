from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *

def profile_view(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'a_users/profile.html', context)

@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)
    context = {'form': form}
    return render(request, 'a_users/profile_edit.html', context)