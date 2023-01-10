from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from uweflixusers.forms import CreateUserForm

# admin - username : c password : adminpassword

def login_user(request):
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            messages.success(request, ("Invalid login details, please try again"))
            return redirect("login-user")
    else:
        return render(request, "authenticate/login.html")
    
def logout_user(request):
    
    logout(request)
    messages.success(request, ("You have logged out"))
    return redirect("home")

def create_user(request):
    
    if request.method=="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']        
            user = authenticate(username = username, password = password)
            login(request,user)
            messages.success(request,("Sign up success!"))
            return redirect("home")
    else:
        form = CreateUserForm()
    return render(request, "authenticate/create_user.html",{"form":form})
    
