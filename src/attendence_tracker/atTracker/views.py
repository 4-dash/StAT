from django.shortcuts import render, reverse, get_object_or_404
from .models import Student
from django.http import HttpResponseRedirect
from .forms import AddStudent, EditStudent

def home(request) :
    students = Student.objects.all()
    return render(request, 'home.html', {"students" : students})

def student(request, id) :
    st = get_object_or_404(Student, id=id)
    return render(request, 'student.html', {"st" : st, "id" : id})

def add_student(request) :
    if request.method == "POST" :
        form = AddStudent(request.POST)
        
        if form.is_valid() :
            try :
                st = Student.objects.create(
                    firstname=form.cleaned_data["firstname"],
                    surname=form.cleaned_data["surname"],
                    attendence_count=0
                )
                return HttpResponseRedirect(reverse('student', args=[st.id]))
            except Exception :      
                return render(request, "add_stud.html", {"form": form, "warning": "An error occured. Student might not have been added."})
    
    form = AddStudent()
    return render(request, "add_stud.html", {"form": form, "warning": ""})


def edit_student(request, id) :
    if request.method == "POST" :
        st = get_object_or_404(Student, id=id)
        form = EditStudent(request.POST, instance = st)

        if form.is_valid() :
            form.save()
            return HttpResponseRedirect(reverse("student", args=[id]))
                

    st = get_object_or_404(Student, id=id)
    form = EditStudent(initial={"firstname": st.firstname, "surname": st.surname, "attendence_count": st.attendence_count})
    return render(request, "edit_stud.html", {"form" : form, "st" : st, "id" : id})