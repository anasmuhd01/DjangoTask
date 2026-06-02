from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,FormView,CreateView
from student.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login
from student.forms import StudentdetailsForm
from student.models import StudentDetails

# Create your views here.

class SigninView(FormView):
    template_name = 'signin.html'
    form_class = SigninForm

    def post(self, req):
        form_data = SigninForm(req.POST)
        if form_data.is_valid():
            uname = form_data.cleaned_data['username']
            pas = form_data.cleaned_data['password']
            user = authenticate(req,username = uname, password = pas)
            if user:
                login(req,user)
                return redirect('shome')
            else: 
                return render(req,'signin.html')


class SignupView(CreateView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('shome')


class HomeView(View):
    def get(self,req):
        data = StudentDetails.objects.all()
        return render(req,'studenthome.html',{'sdetails':data})


class CreateStudentView(CreateView):
    template_name = 'addstudent.html'
    form_class = StudentdetailsForm
    success_url = reverse_lazy('shome')

class EditStudentView(View):
    def get(self,req,**kwargs):
        id = kwargs.get('id')
        form_data = StudentDetails.objects.get(id=id)
        #use only if data is passed as in djangoform model
        # form_data = StudentdetailsForm(instance=qset)
        return render(req,"editstudent.html",{'form_data':form_data})
    
    def post(self,req,**kwargs):
        id = kwargs.get('id')
        student = StudentDetails.objects.get(id=id)
        student.name = req.POST.get('name')
        student.dob = req.POST.get('dob')
        student.div = req.POST.get('div')
        student.year = req.POST.get('year')
        if req.FILES.get('img'):
            student.img = req.FILES.get('img')

        student.save()
        return redirect('shome')
        

    
    


    