from django.shortcuts import render, reverse
from .models import Student
from django.http import HttpResponseRedirect
from .forms import AddStudent

def home(request) :
    students = Student.objects.all()
    return render(request, 'home.html', {"students" : students})

def student(request, id) :
    stud = Student.objects.get(id=id)
    return render(request, 'student.html', {"stud" : stud})

def add_student(request) :
    if request.method == "POST" :
        form = AddStudent(request.POST)
        
        if form.is_valid() :
            try :
                st = Student.objects.create(
                    firstname=form.cleaned_data["firstname"],
                    surname=form.cleaned_data["surname"],
                    attendance_count=0
                )
                return HttpResponseRedirect(reverse('student', args=[st.id]))
            except Exception :      
                return render(request, "add_stud.html", {"form": form, "warning": "An error occured. Student might not have been added."})
    
    form = AddStudent()
    return render(request, "add_stud.html", {"form": form, "warning": ""})