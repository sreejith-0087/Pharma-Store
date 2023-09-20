from django.contrib import messages
from django.shortcuts import render, redirect
from staff.models import Medicine,Categories
from security.models import RetailerDetails
from django.contrib.auth.decorators import login_required
from shop.models import Feedback
from cart.models import Orders,CartItem,Cart,ProductOrders
# Create your views here.



def AllMedicines(request,link=None):
    if link is not None:
        cat=Categories.objects.get(link=link)
        med=Medicine.objects.filter(category=cat.id)
    else:
        med=Medicine.objects.all()
    return render(request,'shop.html',{'medicines':med})


def MedDetail(request,med_id):
    medicine=Medicine.objects.get(id=med_id)
    fed=Feedback.objects.filter(medicine=med_id)
    return render(request,"shop-single.html",{'med':medicine,'feedbacks':fed})

def Contact(request):
    return render(request,'contact.html')


def About(request):
    return render(request,'about.html')


@login_required(login_url='security:retailer_login')
def Product_search(request):
    query = request.GET.get('q')
    if query:
        results = Medicine.objects.filter(medicine__icontains=query)
    else:
        results = []
    return render(request, 'shop.html', {'medicines': results})



@login_required(login_url='security:retailer_login')
def Retailer_profile(request):
    profile = RetailerDetails.objects.get(id=request.user.id)
    return render(request, 'retailer_profile.html', {'profile': profile})

@login_required(login_url='security:retailer_login')
def AddFeedback(request,med_id):
    if request.method=="POST":
        fed=request.POST['feedback']
        medicine=Medicine.objects.get(id=med_id)
        user=RetailerDetails.objects.get(id=request.user.id)
        if Feedback.objects.filter(user=user,medicine=medicine).exists():
            messages.info(request,"* Review already added")
            return redirect("shop:med_single", med_id)
        else:
            Feedback(user=user,medicine=medicine,feedback=fed).save()
            return redirect("shop:med_single",med_id)

@login_required(login_url='security:retailer_login')
def order_confirmation(request):
    order = Orders.objects.filter(user=request.user.id)
    orderd_products = ProductOrders.objects.filter(order__in=order)
    return render(request, 'order_confirmation.html', {'order_items':orderd_products})


