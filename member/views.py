from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def signup(request):
    if request.user.is_authenticated:
        return redirect("member")

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "🎉 Account created successfully.")
            return redirect("login")

        else:
            messages.error(request, "Please correct the errors below.")

    else:
        form = SignUpForm()

    return render(request, "member/signup.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("member")

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("member")

        else:
            messages.error(request, "Username or Password is incorrect")

    return render(request, "member/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("login")


@login_required(login_url='login')
def member(request):
    return render(request, 'member/home.html')