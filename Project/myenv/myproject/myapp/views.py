from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def shop(request):
    return render(request,'shop.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')

def login(request):
    return render(request,'login.html')





def signup(request):
    if request.method == "POST":
        try:
            
            user = User.objects.get(email = request.POST['email'])
            msg  = "Email is already Exits! "
            return render(request,'signup.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],  
                    mobile = request.POST['mobile'],
                    password = request.POST['password'],
                    countryName = request.POST['countryName'],
                    
                )
                return render(request,'login.html')
            else:
                msg = "Password and confirm Password doesn't match!"
                return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')
    
def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            
            if user.password == request.POST['password']:
                request.session['email']= user.email
                return render(request,'index.html')
            else:
                msg = "Password doesn't match !!"
                return render(request,'login.html',{'msg':msg})
        except:
            msg = "Email dosen't match !!"
            return render(request,'login.html',{'msg':msg})
            
    
    else:
        return render(request,'login.html')
        