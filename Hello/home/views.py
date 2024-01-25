from django.shortcuts import render
from home.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html' )
def home(request):
    return render(request,'home.html' )
def login(request):
    return render(request,'login.html' )

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact = Contact(name = name, email=email, message = message)
        contact.save()
    return render(request,'contact.html' )