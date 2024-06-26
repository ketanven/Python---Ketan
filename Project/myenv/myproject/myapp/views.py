from django.shortcuts import render,redirect
from .models import *
import random
import requests
from django.core.files.storage import FileSystemStorage


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

def profilepage(request):
    user = User.objects.get(email=request.session['email'])
    
    if request.method == "POST":
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.mobile = request.POST['mobile']
        user.countryName = request.POST['countryName']
        
        try:
            user.profile = request.FILES['profile']
            user.save()
            request.session['profile'] = user.profile.url 
            
        except:
            user.save()
            if user.usertype == "buyer":
                return redirect("index")
            else:
                return redirect("sindex")
    else:
        
        if user.usertype == "buyer":
            return render(request, 'profile.html', {'user': user})
        else:
            return render(request, 'Sellerprofile.html', {'user': user})
         





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
                    profile = request.FILES['profile'],
                    usertype = request.POST['usertype']
                    
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
                request.session['profile'] = user.profile.url
                if user.usertype == "buyer":
                    return render(request,'index.html')
                else:
                    return render(request,'SellerIndex.html')

            else:
                msg = "Password doesn't match !!"
                return render(request,'login.html',{'msg':msg})
        except:
            msg = "Email dosen't match !!"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
    

def logout(request):
    del request.session['email']
    del request.session['profile']

    return redirect("login")

def cpass(request):
    user = User.objects.get(email=request.session['email'])
    if request.method=="POST":
        try:
            
            if user.password == request.POST['password']:
                if request.POST['npassword'] == request.POST['cpassword']:
                    user.password = request.POST['npassword']
                    user.save()
                    return redirect("logout")
                else:
                    msg = "Password And Confirm Passsword Doesn't Match "
                    if user.usertype =="buyer":
                        return render(request,'cpass.html',{"msg":msg})
                    else:
                        return render(request,'SellerCPassword.html',{"msg":msg})

                        
            else:
                msg = "Old Password Doesn't Match "
                if user.usertype == "buyer":
                   return render(request,'cpass.html',{"msg":msg})
                else:
                    return render(request,'SellerCPassword.html',{"msg":msg})
          
        except:
            if user.usertype == "buyer":
                return render(request,"cpass.html")
            else:
                return render(request,"SellerCPassword.html")
    
                    
    else:    
        if user.usertype == "buyer":        
            return render(request,"cpass.html")
        else:
            return render(request,"SellerCPassword.html")



def fpass(request):
    if request.method== "POST":
        
        try:
             
            user = User.objects.get(mobile = request.POST['mobile'])
            mobile = request.POST['mobile']
            otp = random.randint(1001,9999)
            
            resp = requests.post('https://textbelt.com/text', {
            'mobile': str(mobile),
            'message': otp,
            'key': 'textbelt',
        })
            request.session['mobile']=mobile
            request.session['otp'] = otp
            print(resp.json())
            return render(request,'otp.html')   

        except:
            msg = "Mobile Number Doesn't Exits!!" 
            return render(request,'fpass.html',{"msg":msg})  
    else:
        return render(request,'fpass.html')  

           


def otp(request):
    otp = int(request.session['otp'])
    uotp = int(request.POST['uotp'])
    try:
        
        if otp == uotp:
            del request.session['otp']
            return render(render,"newpass.html")
        else:
            msg = "Invalid otp!!"
            return render(request,"otp.html",{"msg":msg})
    except:
        return render(request,'otp.html')
    
    
    
#___________________________________________________________
#seller


def sindex(request):
    return render(request,"SellerIndex.html")




def addproduct(request):
    if request.method == "POST":
        user = User.objects.get(email=request.session['email'])
        try:
            print("hello")
            Product.objects.create(
                user=user,
                pcategory=request.POST['pcategory'],
                productname=request.POST['productname'],
                pprice=request.POST['pprice'],
                pdesc=request.POST['pdesc'],
                productimage=request.FILES['productimage'], # Assuming productimage is a file upload
            )
            return redirect("viewProduct")
        except Exception as e:
            print(e)
            msg = "Error adding product. Please try again."
            return render(request, "SellerIndex.html", {"msg": msg})
    return render(request, "SellerAddProducts.html")

    
def viewproduct(request):
    user = User.objects.get(email=request.session['email'])
    product = Product.objects.filter(user=user)
    return render(request, "ViewProduct.html", {"product": product})

