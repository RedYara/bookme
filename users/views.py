from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "registration/register.html", {"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have singed up successfully.")
            login(request, user)
            return redirect("books")
        else:
            return render(request, "registration/register.html", {"form": form})
