from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return render(request,'index.html')

def reg(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        newprofile=Profile(fname=fname,lname=lname,email=email)
        newprofile.save()
        success = 'USER'+ fname + "created successsfully"
        return HttpResponse(success)