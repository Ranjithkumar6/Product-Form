from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from .forms import *


#This Function is for addind and lising
def addshow(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['password']
            reg = User(name=nm,email=em,password=pm)
            reg.save()
            messages.success(request,"Data! Added Successfully")
            fm = StudentRegistration()
            return redirect('/')

    else:
        fm = StudentRegistration()
        stud = User.objects.all()

    return render(request,'Product_app/addandshow.html',{'form':fm,'stu':stud})

#This function is for Delete
def Delete_Data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

#this function is for update
def update_Data(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance= pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')   
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance= pi)
        return render(request,'Product_app/update.html',{'form':fm})
 








