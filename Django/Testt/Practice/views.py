from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def service(request):
    return render(request,'service.html')