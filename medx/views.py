from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
# from django.core.mail import send_mail
from django.contrib import messages
import request
from django.shortcuts import get_object_or_404

# Create your views here.


def home(request):
    return render(request, 'home/home.html', {'':''})

def diabetes_report(request):

    return render(request, 'Diabetes/Report.html', {'':''})

def diabriskpred(request):
    if request.method == 'POST':
        form = Diabetes(request.POST)

        if form.is_valid():
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            total_cholestrol = form.cleaned_data['total_cholestrol']
            hdl_cholestrol = form.cleaned_data['hdl_cholestrol']
            weight =  form.cleaned_data['weight']
            height =  form.cleaned_data['height']
            waist =  form.cleaned_data['waist']
            hip =  form.cleaned_data['hip']
            physically_active =  form.cleaned_data['physically_active']
            eat = form.cleaned_data['eat']
            bp = form.cleaned_data['bp']
            relative_diabetes = form.cleaned_data['relative_diabetes']
            parent_diabetes = form.cleaned_data['parent_diabetes']
            glucose = form.cleaned_data['glucose']
            smoking = form.cleaned_data['smoking']
            heart_disease = form.cleaned_data['heart_disease']
            depression = form.cleaned_data['depression']
            HbA1c = form.cleaned_data['HbA1c']
            haem = form.cleaned_data['haem']
            form.save()
            dic = {'age':age}

    return render(request, 'Diabetes/Report.html')

def contact(request):

    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            form.save()
    return render(request, 'contact/contact.html', {'Title':'Contact Us'},{'':'','message':"Your form was submitted successfully!"})