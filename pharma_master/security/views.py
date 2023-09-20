from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from staff.models import StaffDetails,Medicine
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from security.models import RetailerDetails

# Create your views here.

def Home(request):
    medicines=Medicine.objects.all()
    return render(request,'security/index.html',{"medicines":medicines})

def StaffRegister(request):
    if request.method=="POST":
        f_name=request.POST['fname']
        l_name=request.POST['lname']
        add=request.POST['address']
        mail=request.POST['email']
        contact_number=request.POST['mobile']
        cv=request.FILES['resume']
        image=request.FILES['photo']
        npasswd=request.POST['passwd']
        c_passwd=request.POST['cpasswd']
        if npasswd==c_passwd:
            if User.objects.filter(username=mail).exists():
                messages.info(request, "User already exists")
            else:
                user=User.objects.create_user(username=mail,password=c_passwd)
                user.status=False


                staff=StaffDetails(id=user,first_name=f_name,last_name=l_name,photo=image,address=add,resume=cv,phone=contact_number)
                user.save()
                staff.save()
                subject="Welcome to Pharma master"
                message=f"Dear {f_name} {l_name} , \n I hope this mail finds you well.We delighted to have you in our team .You can use below credentials to login\n" \
                        f"Use Id:  {user.id}\n" \
                        f"Password : {c_passwd}\n" \
                        f"Please change the temporary password while you login"

                send_mail(subject,message=message,from_email=settings.EMAIL_HOST_USER,recipient_list=[user.username],fail_silently=False)
                messages.info(request,f"Your Employee id is {user.id} .Notification mail have send to the employee")
                return redirect("staff:staffdash")
        else:
            messages.error(request, "Passwords dose not match")
    return render(request,"security/register.html")

def StaffLogin(request):
    user=None
    if request.method=="POST":
        id=request.POST['emp_id']
        mail=request.POST['email']
        password=request.POST['passwd']
        user=auth.authenticate(username=mail,id=id,password=password)
        if user is not None and StaffDetails.objects.filter(id=id).exists():
            auth.login(request,user)
            return redirect('staff:staffdash')
        else:
            messages.info(request, "Invalid username or password")
    return render(request,"security/login.html")


def Logout(request):
    auth.logout(request)
    return redirect("/")

# Retailer credential management

def RetailerRegister(request):
    if request.method=="POST":
        f_name=request.POST['c_fname']
        l_name=request.POST['c_lname']
        mail=request.POST['c_email']
        contact=request.POST['phone']
        passwd=request.POST['password']
        cpasswd=request.POST['con_password']
        address=request.POST['address']
        photo=request.FILES['image']
        if passwd==cpasswd:
            if User.objects.filter(username=mail).exists():
                messages.info(request,"User already exists")
            else:
                user=User.objects.create_user(username=mail,password=passwd)
                retailer=RetailerDetails(id=user,first_name=f_name,last_name=l_name,phone=contact,address=address,photo=photo)
                user.is_active=False
                user.save()
                retailer.save()
                messages.info(request,"You can login when admin accepts your request")
        else:
            messages.info(request,"Mismatch password")
    return render(request,"security/retailer-reg.html")


def RetailerLogin(request):
    if request.method=='POST':
        mail = request.POST['c_email']
        password = request.POST['password']
        user = auth.authenticate(username=mail,password=password)

        if user is not None and RetailerDetails.objects.filter(id=user.id).exists():
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
    return render(request,'security/retailer-login.html')