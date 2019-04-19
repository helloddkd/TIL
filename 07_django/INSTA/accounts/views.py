from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from accounts.models import User
from posts.forms import CommentModelForm
from django.contrib.auth import get_user_model
# Create your views here.


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.save())
            return redirect(request.GET.get('next') or 'posts:post_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('posts:post_list')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:post_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:post_list')


def user_detail(request, username):
    user_info = get_object_or_404(User, username=username)
    form = CommentModelForm()
    return render(request, 'accounts/user_detail.html', {'user_info': user_info, 'form': form})


@require_POST
@login_required
def toggle_follow(request, username):
    followee = get_object_or_404(User, username=username)
    user = request.user
    if user != followee:
        if followee in user.followings.all():
            user.followings.remove(followee)
        else:
            user.followings.add(followee)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
