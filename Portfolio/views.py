from django.shortcuts import render, HttpResponse
from datetime import datetime
from Portfolio.models import contact
from django.contrib import messages


# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    return render(request,'index.html',context)
   # return HttpResponse("HomePage")

def Socials(request):
        return render(request,'Socials.html')

def Gallaries(request):
        return render(request,'Gallaries.html')


def Weddings(request):
        return render(request,'Weddings.html')

def Events(request):
        return render(request,'Events.html')

def KidsPhotography(request):
        return render(request,'KidsPhotography.html')
def Photostream(request):
        return render(request,'Photostream.html')



def contact(request):
    if request.method=='POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        Contact=contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        Contact.save()
        messages.success(request, 'Your Message is Successfully Posted.')

    return render(request,'contact.html')

    #return HttpResponse("About")

    #return HttpResponse("faves")
