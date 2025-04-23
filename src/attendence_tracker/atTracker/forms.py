from django import forms

class AddStudent(forms.Form) :
    firstname = forms.CharField(label="First Name", max_length=100, required=True)
    surname = forms.CharField(label="Surname", max_length=100, required=True)