from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.models import User

# from projects.models import USER_MODEL

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password1"]
            user = User.objects.create_user(
                username=username, password=password
            )
            user.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm(request.POST)
    context = {"form": form}
    return render(request, "registration/signup.html", context)
