from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method=="POST":
       contact=Contact()
       name=request.POST.get('name')
       age=request.POST.get('age')
       department=request.POST.get('department')
       contact.name=name
       contact.age=age
       contact.department=department
       contact.save()
       return HttpResponse("<h1>Thanks For Contact Us</h1>")
    
    return render(request,'index.html')
