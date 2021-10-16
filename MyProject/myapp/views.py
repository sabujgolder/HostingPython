from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def base(request):
    return render(request,'base.html')

def index(request):
    val = {'a':'apple','b':'ball'}

    musician = Musician.objects.all()

    dict = {'val':val,'musician':musician}

    dict.update({'text':"It's a text"})

    return render(request,'myapp/index.html',context=dict)

def forms(request):
    form = UserForm()
    dictionary = {'form':form}
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            choice = form.cleaned_data['Multiple_Choice']
            cc= form.cleaned_data['cc_myself']
            dictionary.update({'username':username,'email':email,'submitted': "Yes",'choice':choice,'cc':cc})

    return render(request,'myapp/form.html',context=dictionary)

def artists(request):
    artists = Musician.objects.all()
    return render(request,'myapp/artists.html',{'artists':artists})

def about(request,artist_id):
    albums = Musician.objects.get(pk=artist_id)
    return render(request,'myapp/about.html',{'albums':albums})
