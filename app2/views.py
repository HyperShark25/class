from django.shortcuts import render, redirect
from .models import Student, Teacher, Subject, Enrollment
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SubjectForm, TeacherForm, EnrollmentForm


@login_required
def table(request): # This function displays the all of the data in the database tables
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    subject = Subject.objects.all()
    enroll = Enrollment.objects.all()
    for en in enroll:
        en.subjects = en.subject.all()
        en.students = en.student.all()
        en.teachers = en.teacher.all()
    context = {"student": student, "teacher": teacher, "subject": subject, "enroll": enroll}
    return render(request, "table.html", {"context": context})


@login_required
def create(request): # this function creates a new student record
    if request.method == "POST":
        name = request.POST.get("Name")
        age = request.POST.get("Age")
        address = request.POST.get("Address")
        u = Student.objects.create(name=name, age=age, address=address)
        u.save()
        return redirect("table")
    else:
        return render(request, "create.html")


@login_required
def update_student(request, pk): # this function updates the student record by getting the primary key which is the id
    up = Student.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get("Name")
        age = request.POST.get("Age")
        address = request.POST.get("Address")
        up.name = name
        up.age = age
        up.address = address
        up.save()
        return redirect("table")
    else:
        return render(request, "cs.html", {"up": up})



@login_required
def rst(request, pk): # this function removes the student record by using the primary key as an identifier
    query = Student.objects.get(id=pk)
    query.delete()
    return redirect("table")


@login_required
def TForm(request): # This function creates a new teacher record
    form = TeacherForm()
    if request.method == "POST":
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("table")
    else:
        return render(request, "teacher.html", {"form": form})



@login_required
def update_teacher(request, pk): # this function updates the Teacher record by getting the primary key which is the id
    up = Teacher.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get("Name")
        address = request.POST.get("Address")
        phone = request.POST.get("Phone")
        up.name = name
        up.address = address
        up.phone = phone
        up.save()
        return redirect("table")
    else:
        return render(request, "ut.html", {"up": up})


@login_required
def rt(request, pk): # this function removes the Teacher record by using the primary key as an identifier
    query = Teacher.objects.get(id=pk)
    query.delete()
    return redirect("table")


@login_required
def SubjForm(request): # This function creates a new subject
    form = SubjectForm()
    if request.method == "POST":
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("table")
    else:
        return render(request, "subj.html", {"form": form})


@login_required
def update_subject(request, pk): # this function updates the Teacher record by getting the primary key which is the id
    up = Subject.objects.get(id=pk)
    if request.method == "POST":
        name = request.POST.get("Name")
        description = request.POST.get("Description")
        up.name = name
        up.description = description
        up.save()
        return redirect("table")
    else:
        return render(request, "us.html", {"up": up})


@login_required
def rsubj(request, pk): # this function removes the Teacher record by using the primary key as an identifier
    query = Subject.objects.get(id=pk)
    query.delete()
    return redirect("table")


@login_required
def EnrollForm(request): # This function creates a new encrollment data record which is responsible of connecting the three tables students, teachers and subjects
    form = EnrollmentForm()
    if request.method == "POST":
        form = EnrollmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("table")
    else:
        return render(request, "enroll.html", {"form": form})


@login_required
def update_enroll(request, pk): # this function updates the Teacher record by getting the primary key which is the id
    up = Enrollment.objects.get(id=pk)
    if request.method == "POST":
        subject = request.POST.getlist("Subject")
        student = request.POST.getlist("Student")
        teacher = request.POST.getlist("Teacher")
        up.subject.clear()
        up.student.clear()
        up.teacher.clear()
        for subject0 in subject:
            up.subject.add(subject0)
        
        for student0 in student:
            up.student.add(student0)
        
        for teacher0 in teacher:
            up.teacher.add(teacher0)
        
        up.save()
        return redirect("table")
    else:
        subjects = Subject.objects.all()
        students = Student.objects.all()
        teachers = Teacher.objects.all()
        return render(request, "uenroll.html", {"up": up, "subjects": subjects,  "students": students, "teachers": teachers})


@login_required
def renroll(request, pk): # this function removes the Teacher record by using the primary key as an identifier
    query = Enrollment.objects.get(id=pk)
    query.delete()
    return redirect("table")


@login_required
def search_student(request): # This function is used to search for a specific student by taking the input of the name of the student
    if request.method == "POST":
        name = request.POST.get("Name")
            
        if Student.objects.filter(name=name).exists():
            return redirect("sst", pk=name)
                
        else:
            messages.info(request, "Student not Found")
            return redirect("table")
    else:
        return render(request, "table.html")


@login_required
def search_detail(request, pk): #  Used for the value the search function and returns the user's data of the searched name
    try:
        item2 = Student.objects.get(name=pk)
        if item2 is False:
            return redirect("table")
    except:
        pass
    try:
        item2 = Subject.objects.get(name=pk)
        if item2 is False:
            return redirect("table")
        else:
            return render(request, "ssubj.html", {"item2": item2})
    except:
        pass
    try:
        item2 = Teacher.objects.get(name=pk)
        if item2 is False:
            return redirect("table")
        else:
            return render(request, "ste.html", {"item2": item2})
    except:
        pass
    return render(request, "sst.html", {"item2": item2})


@login_required
def search_teacher(request): # This function is used to search for a specific student by taking the input of the name of the student
    if request.method == "POST":
        name = request.POST.get("TName")
            
        if Teacher.objects.filter(name=name).exists():
            return redirect("sst", pk=name)
                
        else:
            messages.info(request, "Teacher not Found")
            return redirect("table")
    else:
        return render(request, "table.html")


@login_required
def search_subject(request): # This function is used to search for a specific student by taking the input of the name of the student
    if request.method == "POST":
        name = request.POST.get("SubjName")
            
        if Subject.objects.filter(name=name).exists():
            return redirect("ssubj", pk=name)
                
        else:
            messages.info(request, "Subject not Found")
            return redirect("table")
    else:
        return render(request, "table.html")
