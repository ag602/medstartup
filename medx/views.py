from django.shortcuts import render
from .forms import *
from django.http import HttpResponseRedirect
# from django.core.mail import send_mail
from django.contrib import messages
import request

# Create your views here.


def home(request):
    return render(request, 'home/home.html', {'':''})

def diabriskpred(request):
    return render(request, 'diabriskpred.html', {'':''})

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