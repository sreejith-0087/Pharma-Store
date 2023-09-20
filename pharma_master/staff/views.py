from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils.text import slugify
from shop.models import Feedback
from staff.models import Categories,Medicine,Brand,StaffDetails,PendingOrders
from staff.forms import MedicineForm
from django.contrib.auth.decorators import login_required
from cart.models import Orders,ProductOrders
# Create your views here.

@login_required(login_url='security:staff_login')
def StaffDashboard(request):
    return render(request,"staff-dashboard.html")

@login_required(login_url='security:staff_login')
def AddCategory(request):
    if request.method=="POST":
        name=request.POST['category']
        link=slugify(name)
        cat=Categories(category=name,link=link)
        cat.save()
        return redirect('staff:add_medicine')
    return render(request,"add-category.html")

@login_required(login_url='security:staff_login')
def AddMedicine(request):
    medi_form=MedicineForm()
    if request.method=="POST":
        medi_form=MedicineForm(request.POST or None,request.FILES or None)
        if medi_form.is_valid():

            medi_form.save()
            return redirect("staff:all_medicines")
    return render(request,"add-medicine.html",{"myform":medi_form})

@login_required(login_url='security:staff_login')
def AllMedicines(request):
    medicines=Medicine.objects.all()
    return render(request,"all-medicines.html",{"medicines":medicines})

@login_required(login_url='security:staff_login')
def UpdateMedicine(request,mid):
    medicine=Medicine.objects.get(id=mid)
    medi_form = MedicineForm(request.POST or None, request.FILES or None,instance=medicine)
    if request.method=="POST":
        if medi_form.is_valid():
            medi_form.save()
            return redirect("staff:all_medicines")
    return render(request,"update-medicine.html",{"form":medi_form})

@login_required(login_url='security:staff_login')
def DeleteMedicine(request,mid):
    medicine=Medicine.objects.get(id=mid)
    medicine.delete()
    return redirect("staff:all_medicines")

@login_required(login_url='security:staff_login')
def MedicineDetail(request,mid):
    medicine=Medicine.objects.get(id=mid)
    fed = Feedback.objects.filter(medicine=mid)
    return render(request,"medicine-detail.html",{'medicine':medicine,'feedbacks':fed})


@login_required(login_url='security:staff_login')
def view_profile(request):
    profile = StaffDetails.objects.get(id=request.user.id)
    return render(request, 'view_profile.html', {'profile': profile})


@login_required(login_url='security:staff_login')
def product_search(request):
    query = request.GET.get('q')
    if query:
        results = Medicine.objects.filter(medicine__icontains=query)
    else:
        results = []
    return render(request, 'all-medicines.html', {'medicines': results})

@login_required(login_url='security:staff_login')
def AddWishlist(request,mid,count):
    medicine=Medicine.objects.get(id=mid)
    wishlist=PendingOrders(medicine=medicine.id,count=count)
    return redirect("staff:all_medicines",{'wishlist':wishlist})

def ViewOrders(request):
    orders=Orders.objects.filter(delivery_status=False)
    return render(request,"view-orders.html",{"orders":orders})

def OrderDetail(request,id):
    order=Orders.objects.get(id=id)
    products=ProductOrders.objects.filter(order=order)
    return render(request,"order-detail.html",{'products':products})

