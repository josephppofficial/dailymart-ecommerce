from django.shortcuts import render,redirect
from adminapp.models import *
from userapp.models import Cart, Checkout, Contact, Registration
from django.db.models.aggregates import Sum
# Create your views here.
def user(request):
    return render(request,'user.html')
def cardcategory(request):
    data=Category.objects.all()
    return render(request,'cardcategory.html',{'data':data})
def cardproduct(request,category):
    if(category == "all"):
      data1=Product.objects.all()
    else:
        data1 = Product.objects.filter(category=category)
    data=Category.objects.all()
    return render(request,'cardproduct.html',{'data1':data1,'data':data})
def single(request,id):
    data=Product.objects.filter(id=id)
    return render(request,'singleproduct.html',{'data':data})
def contact(request):
    return render(request,'contact.html')
def contact_page(request):
    if request.method=="POST":
        yourname=request.POST['yourname']
        youremail=request.POST['youremail']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']
        feedback=Contact(yourname=yourname,youremail=youremail,phone=phone,subject=subject,message=message)
        feedback.save()
    return redirect('contact')
def registration(request):
    return render(request,'registration.html')
def registration_page(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        phone=request.POST['phone']
        register=Registration(username=username,email=email,phone=phone,password=password)
        register.save()
    return redirect('registration')
def login(request):
    return render(request,'login.html')
def userlogout(request):
    del request.session ['uid']
    del request.session['username']
    del request.session['email']
    del request.session['password']
    del request.session['phone']
    return redirect('login')
def publicdata(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if Registration.objects.filter(username=username,password=password).exists():
           register = Registration.objects.filter(username=username,password=password).values('id','email','phone').first()
           request.session['uid'] = register['id']
           request.session['email'] = register['email'] 
           request.session['username'] = username
           request.session['password'] = password
           request.session['phone'] = register['phone']
           return redirect('user') 
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('login')

def home(request):
    data = Category.objects.all()  
    data1 = Product.objects.all() 
     
    return render(request, 'home.html', {'data': data, 'data1': data1})
def cart(request):
    c = request.session.get('uid')
    cart = Cart.objects.filter(cartuser=c,status=0)
    a = Cart.objects.filter(cartuser=c,status=0).aggregate(total_sum=Sum('total'))
    return render(request, 'cart.html', {'cart': cart,'a':a})
def checkout(request):
    c = request.session.get('uid')
    check = Cart.objects.filter(cartuser=c,status=0)
    b = Cart.objects.filter(cartuser=c,status=0).aggregate(total_sum=Sum('total'))
    return render(request, 'checkout.html',{'check':check,'b':b})
def cart_data(request,id):
    if request.method=="POST":
        user_id = request.session.get('uid')
        quantity = request.POST['quantity']
        total = request.POST['total']
        cart = Cart(cartuser=Registration.objects.get(id=user_id), cartproduct=Product.objects.get(id=id),quantity=quantity,total=total)
        cart.save()
    return redirect('cart')
def deleted(request, id):
    cart = Cart.objects.filter(id=id)
    cart.delete()
    return redirect('cart')
def checkoutdata(request):
    if request.method=="POST":
        checkoutid = request.session.get('uid')
        address = request.POST.get('address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        postcode = request.POST.get('pincode')

        buy = Cart.objects.filter(cartuser=checkoutid,status=0)

        for i in buy :
            check = Checkout(usercheckout=Registration.objects.get(id=checkoutid), checkoutcart=Cart.objects.get(id=i.id),address=address,city=city,country=country,postcode=postcode)
            check.save()
            Cart.objects.filter(id=i.id).update(status=1)
    return redirect('success') 
def success(request):
    s = request.session.get('uid')
    success = Checkout.objects.filter(usercheckout=s)
    return render (request,'success.html',{'success':success})
def about(request):
    return render(request,'about.html')