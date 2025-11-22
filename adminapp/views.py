from atexit import register
from django.shortcuts import render,redirect

from userapp.models import Checkout, Contact, Registration
from.models import *
# Create your views here.
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
def adminapp(request):
    data = Category.objects.all().count  
    data1 = Product.objects.all().count
    register = Registration.objects.all().count
    feedback = Contact.objects.all().count 
    order = Checkout.objects.all().count
    return render(request,'adminapp.html',{'data': data, 'data1': data1, 'register':register, 'feedback':feedback, 'order':order})
def addcategory(request):
    return render(request,'addcategory.html')
def viewcategory(request):
    data=Category.objects.all()
    return render(request,'viewcategory.html',{'data':data})
def category_data(request):
    if request.method=="POST":
       category=request.POST['category']
       description=request.POST['description']
       image=request.FILES['image']
       data=Category(category=category,description=description,image=image)
       data.save()
    return redirect('addcategory')
def delete(request, id):
    data = Category.objects.filter(id=id)
    data.delete()
    return redirect('viewcategory')
def edit(request,id):
    data=Category.objects.filter(id=id)
    return render(request,'edit.html',{'data':data})
def update(request,id):
     if request.method=="POST":
        category=request.POST['category']
        description=request.POST['description']
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=id).image
        Category.objects.filter(id=id).update(category=category,description=description,image=file)
        return redirect('viewcategory')
def addproduct(request):
    data1= Category.objects.all()
    return render(request,'addproduct.html',{'data1': data1})
def viewproduct(request):
    data1=Product.objects.all()
    return render(request,'viewproduct.html',{'data1':data1})
def product_data(request):
    if request.method=="POST":
       product=request.POST['product']
       price=request.POST['price']
       category=request.POST['category']
       image=request.FILES['image']
       data1=Product(product=product,price=price,category=category,image=image)
       data1.save()
    return redirect('addproduct')
def updation(request,id):
     if request.method=="POST":
        product=request.POST['product']
        price=request.POST['price']
        category=request.POST['category']
     try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
     except MultiValueDictKeyError:
            file = Product.objects.get(id=id).image
     Product.objects.filter(id=id).update(product=product,price=price,category=category,image=file)
     return redirect('viewproduct')
def clear(request, id):
    data1 = Product.objects.filter(id=id)
    data1.delete()
    return redirect('viewproduct')
def editproduct(request,id):
    data=Product.objects.filter(id=id)
    return render(request,'editproduct.html',{'data':data})
def contact_table(request):
    feedback=Contact.objects.all()
    return render(request,'contact_table.html',{'feedback':feedback})
def table_registration(request):
    register=Registration.objects.all()
    return render(request,'table_registration.html',{'register':register})
def order(request):
    order=Checkout.objects.all()
    return render(request,'orders.html',{'order':order})
