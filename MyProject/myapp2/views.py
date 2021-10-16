from django.shortcuts import render,redirect
from myapp2.forms import validator_form
from myapp2.forms import *

def home(request):
    form = validator_form()
    dictionary={'form':form}

    if request.method =="POST":
        form = validator_form(request.POST)
        dictionary.update({'form':form})

    return render(request,'myapp2/home.html',context=dictionary)

def NewUserForm(request):

    form = FormForNewUser(initial={'username': 'Enter Username','Another_comment':'Enter Your Comment'})
    dict={'form':form}

    if request.method == "POST":
        form = FormForNewUser(request.POST)
        dict.update({'form':form})
        
        if form.is_valid():
            form.save(commit=True)
            return redirect('modelform')

    return render(request,'myapp2/newform.html',context=dict)
