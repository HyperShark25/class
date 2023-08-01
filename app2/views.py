from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def table(request):
    item = Student.objects.all()
    return render(request, "table.html", {"item": item})


@login_required
def update_student(request, pk):
    up = Student.objects.get(id=pk)
    if request.method == "POST":
        fn = request.POST.get("First Name")
        ln = request.POST.get("Last Name")
        age = request.POST.get("Age")
        term = request.POST.get("Term")
        gpa = request.POST.get("GPA")
        up.fn = fn
        up.ln = ln
        up.age = age
        up.term = term
        up.save()
        return redirect("table")
    else:
        return render(request, "cs.html", {"up": up})


@login_required
def create(request):
    if request.method == "POST":
        fn = request.POST.get("First Name")
        ln = request.POST.get("Last Name")
        age = request.POST.get("Age")
        term = request.POST.get("Term")
        gpa = request.POST.get("GPA")
        u = Student.objects.create(fn=fn, ln=ln, age=age, term=term, gpa=gpa, user=request.user)
        u.save()
        return redirect("table")
    else:
        return render(request, "create.html")

@login_required
def search_student(request):
    if request.method == "POST":
        fn = request.POST.get("Name")
        ln = request.POST.get("Name")
            
        if Student.objects.filter(fn=fn).exists():
            return redirect("sst", pk=fn)
        
        elif Student.objects.filter(ln=ln).exists():
            return redirect("sst", pk=ln)    
        
        else:
            messages.info(request, "Student not Found")
            return redirect("table")
    else:
        return render(request, "table.html")

@login_required
def student_detail(request, pk): #  Used for the value the search function returns in case the user searched either through first name or last name
    try:
        item2 = Student.objects.get(fn=pk)
    except:
        item2 = Student.objects.get(ln=pk)
    return render(request, "sst.html", {"item2": item2})


@login_required
def rst(request, pk):
    query = Student.objects.get(id=pk)
    query.delete()
    return redirect("table")
