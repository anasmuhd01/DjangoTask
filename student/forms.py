from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from student.models import StudentDetails

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class SigninForm(forms.Form):
    username = forms.CharField(max_length =100)
    password = forms.CharField(max_length=100)

class StudentdetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = '__all__'