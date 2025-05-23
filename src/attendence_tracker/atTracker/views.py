from django.shortcuts import render, reverse, get_object_or_404, redirect
from .models import Student
from django.http import HttpResponseRedirect
from .forms import AddStudent, EditStudent
from django.contrib import messages

def home(request) :
    students = Student.objects.all()
    return render(request, 'home.html', {"students" : students})

def student(request, id) :
    # not in major use
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
                messages.success(request, f"Student {st.firstname} {st.surname} has been added.")

                return HttpResponseRedirect(reverse('edit_student', args=[st.id]))

            except Exception :
                messages.error(request, "An error has occured!")     
                return redirect("home")
        else :
            messages.error(request, "Given data is not vaild!")
    
    form = AddStudent()
    return render(request, "add_stud.html", {"form": form})


def edit_student(request, id) :
    if request.method == "POST" :
        st = get_object_or_404(Student, id=id)
        form = EditStudent(request.POST, instance = st)

        if form.is_valid() :
            form.save()
            messages.success(request, f"Student {st.firstname} {st.surname} has been modified.")
            return HttpResponseRedirect(reverse("home"))
        else :
            messages.error(request, "Given data is not vaild!")
                

    st = get_object_or_404(Student, id=id)
    form = EditStudent(initial={"firstname": st.firstname, "surname": st.surname, "attendence_count": st.attendence_count})
    return render(request, "edit_stud.html", {"form" : form, "st" : st, "id" : id})



def del_student(request, id) :
    if request.method == "POST" :
        st = get_object_or_404(Student, id=id)
        name, surname = st.firstname, st.surname
        st.delete()
        messages.success(request, f"Student {name} {surname} was deleted.")
        return redirect(home)

    return HttpResponseRedirect(reverse("edit_student", args=[id]))