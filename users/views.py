from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Profile


def index(request):
    return render(request, 'users/index.html')


@login_required
def profile(request):
    user = get_object_or_404(Profile, pk=request.user.id)
    print(user)
    return render(request, 'users/profile.html', {'profile': user})
