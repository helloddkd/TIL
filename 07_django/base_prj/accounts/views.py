from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from IPython import embed
# Create your views here.


def index(request):
    return render(request, 'accounts/index.html')


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #저장되었으면 그 유저 로그인시켜라
            return redirect('accounts:index')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})


def signin(request):
    #이미로그인했는데 또한다하면
    if request.user.is_authenticated:
        return redirect('accounts:index')
    #로그인시켜주세요
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if request.Get.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('accounts:index')
    #로그인 화면주세요
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/signin.html', {'form':form})


def signout(request):
    logout(request)
    return redirect('accounts:index')



