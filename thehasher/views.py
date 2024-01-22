from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import HashForm

from .models import HashFromUser
# Create your views here.

def index(request):
    hashinputs = HashFromUser.objects.all()
    context = {"hashinputs":hashinputs}
    return render(request, "thehasher/index.html", context)

def unhash(request):
    if request.method == "POST": 
        form = HashForm(request.POST)
        if form.is_valid(): 
            print(form.cleaned_data)
        return redirect('/thehasher')
    else: 
        form = HashForm()
        context = {"form":form}
    return render(request, "thehasher/unhash.html", context)