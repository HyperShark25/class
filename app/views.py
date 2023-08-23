from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

UM = get_user_model()


def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("Username")
        email = request.POST.get("Email")
        date_of_birth = request.POST.get("Birthday")
        password = request.POST.get("Password")
        password2 = request.POST.get("Confirm Password")
        
        
        if password == password2:
            if UM.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect("register")
            
            elif UM.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect("register")
            
            else:
                user = UM.objects.create_superuser(username=username, email=email, password=password, date_of_birth=date_of_birth)
                user.save()
                return redirect("login")
        
        else:
            messages.info(request, "Passwords don't match")
            return redirect("register")
        
    else:
        return render(request, "register.html")



def login(request):
    if request.method == "POST":
        email = request.POST.get("Email")
        password = request.POST.get("Password")
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            user_id = request.user.id
            return redirect(reverse("detail", args=[user_id]))
        
        else:
            messages.info(request, "Credentials Invalid")
            return redirect("login")
    
    else:
        return render(request, "login.html")



def logout(request):
    auth.logout(request)
    return redirect("/")


@login_required
def detail(request, pk):
    item = UM.objects.get(id=pk)
    return render(request, "detail.html", {"item": item})
