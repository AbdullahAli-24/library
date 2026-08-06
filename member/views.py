from django.shortcuts import render, redirect
from books.models import Favorite
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm
from books.models import Book
from loan.models import Loan

def signup(request):
    if request.user.is_authenticated:
        return redirect("member")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success( request, "Account created successfully.")
            return redirect("login")
        else:
            messages.error( request, "Please correct the errors below.")
    else:
        form = SignUpForm()
    return render( request, "member/signup.html", { "form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("member")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate( request, username=username, password=password )
        if user is not None:
            login(request, user)
            messages.success( request,"Welcome back.")
            return redirect("member")
        else:
            messages.error( request, "Invalid username or password." )
    return render( request, "member/login.html" )

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    messages.success( request, "Logged out successfully.")
    return redirect("login")

@login_required(login_url="login")
def member(request):
    total_books = Book.objects.count()
    borrowed_books = Loan.objects.filter(
        returned=False
    ).count()
    available_books = Book.objects.filter(
        available_quantity__gt=0
    ).count()
    total_users = User.objects.count()
    latest_books = Book.objects.order_by("-id")[:6]
    favorite_books = Favorite.objects.filter(
        user=request.user
    ).count()
    return render( request, "member/home.html", {

            "total_books": total_books,
            "borrowed_books": borrowed_books,
            "available_books": available_books,
            "total_users": total_users,
            "latest_books": latest_books,
            "favorite_books": favorite_books,
        })