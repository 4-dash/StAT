from django import forms
from .models import Student

class AddStudent(forms.Form) :
    firstname = forms.CharField(label="First Name", max_length=100, required=True)
    surname = forms.CharField(label="Surname", max_length=100, required=True)


class EditStudent(forms.ModelForm) :
    firstname = forms.CharField(label="First Name", max_length=100, required=True)
    surname = forms.CharField(label="Surname", max_length=100, required=True)
    attendence_count = forms.IntegerField(label="Attended class count", min_value=0, required=True)

    class Meta :
        model = Student
        fields = ["firstname", "surname", "attendence_count"]