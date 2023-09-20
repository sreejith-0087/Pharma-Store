from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from staff.models import Medicine
from . models import Cart,CartItem,Orders,ProductOrders
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from shop.models import RetailerDetails

@login_required(login_url="security:retailer_login")
def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

@login_required(login_url="security:retailer_login")
def add_cart(request,product_id):
    user=RetailerDetails.objects.get(id=request.user.id)
    product=Medicine.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(user=request.user.id)
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_cart_id(request),user=user
        )
        cart.save()
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

@login_required(login_url="security:retailer_login")
def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(user=request.user.id)
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter +=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

@login_required(login_url="security:retailer_login")
def cart_remove(request,product_id):
    cart=Cart.objects.get(user=request.user.id)
    product=get_object_or_404(Medicine,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity >1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')

@login_required(login_url="security:retailer_login")
def full_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_id(request))
    product=get_object_or_404(Medicine,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')

@login_required(login_url="security:retailer_login")
def Checkout(request,total=0,counter=0):
    user_detail=RetailerDetails.objects.get(id=request.user.id)
    user=Cart.objects.get(user=request.user.id)
    cart_items=CartItem.objects.filter(cart=user,active=True)
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.quantity)
        counter += cart_item.quantity
    return render(request,"checkout.html",{"cart_items":cart_items,'total':total,'user_detail':user_detail})


@login_required(login_url="security:retailer_login")
def PlaceOrder(request,total_amount=0):
    user_detail=RetailerDetails.objects.get(id=request.user.id)
    cart=Cart.objects.get(user=request.user.id)
    orders=Orders(user=user_detail)
    orders.save()
    cart_items = CartItem.objects.filter(cart=cart, active=True)
    for cart_item in cart_items:
        medicine=Medicine.objects.get(id=cart_item.product.id)
        total_amount=total_amount+medicine.price
        ProductOrders(order=orders,product=medicine,quantity=cart_item.quantity).save()
    cart.delete()
    orders.amount=total_amount
    orders.save()
    return render(request,"thankyou.html")

@login_required(login_url="security:retailer_login")
def razorpaycheck(request,total_price=0):
    cart=Cart.objects.filter(user=request.user)
    for items in cart:
        medicine = Medicine.objects.get(id=items.product.id)
        total_price = total_price + medicine.price

    return JsonResponse({
        'total_price':total_price
    })






