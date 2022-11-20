from django.shortcuts import render,redirect
from .models import *

def index(request):
    if request.method=='POST':
        eml=request.POST['emal']
        txt=request.POST['utxt']
        obj=userprofiles(email=eml,text=txt)
        obj.save()
    return render (request,'index.html')