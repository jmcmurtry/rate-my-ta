import email
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import SignupForm
from .models import addUser


# Create your views here.
def showPage(request):
    submitbutton= request.POST.get("submit")

    full_name=''
    email=''
    password=''
    # connect to db
    # pass to html page
    # return render(request, 'main.html')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            addUser(full_name,email,password)
    else:
        form = SignupForm()
    context = {'form': form, 'full_name':full_name,'email':email,'password':password,'submitbutton':submitbutton}
    return render( request, 'main.html', context)


def showNextPage(request):
    return render(request, 'done.html')