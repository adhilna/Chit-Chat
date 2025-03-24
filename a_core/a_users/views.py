from django.shortcuts import render

def profile_view(request):
    profile = request.user.profile
    context = {'profile': profile}
    return render(request, 'a_users/profile.html', context)
