from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user

from profiles.models import Status

from django.contrib import messages



def home_view(request):
    return render(request, 'main/home.html')

# получение данных из бд
def register(request):
    return render(request, "main/register.html")
 # сохранение данных в бд
@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name = 'user')
            user.groups.add(group)
            Status.objects.create(
                user=user
            )
            messages.success(request,'Registration successful.')

            return redirect('login')
		
    context = {'form': form}
    return render(request, "main/register.html", context)


@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('posts:posts')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, "main/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')