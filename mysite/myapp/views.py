from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    return HttpResponse("helo world")

# for all products
def products(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'myapp/index.html',context)
    
# for a single product
def product_detail(request,id):
    product=Product.objects.get(id=id)
    context={
        'product':product
    }
    return render(request,'myapp/detail.html',context)

# add product
def add_product(request):
    if request.method =='POST':
    #variable                 name and id passed
       name = request.POST.get('name')
       price = request.POST.get('price')
       desc = request.POST.get('desc')
       image = request.FILES['upload']
       product = Product(name=name, price=price, desc=desc, image=image)
       product.save()
    return render(request,'myapp/addproduct.html') 

# update product
def update_product(request,id):
    # this code below will help display the product detail to be edited
    product= Product.objects.get(id=id)
    if request.method == 'POST':
        # so here we edit what was submitted on form as product.name, desc, etc 
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.desc = request.POST.get('desc')
        product.image = request.FILES['upload']
        product.save()
        return redirect('/myapp/products')
    context={
        'product':product
    }
    return render(request,'myapp/updateproduct.html',context)

# delete product
def delete_product(request,id):
    product=Product.objects.get(id=id)
    context={
        'product':product
    }
    if request.method =='POST':
        product.delete()
        return redirect('/myapp/products')
    return render(request,'myapp/delete.html',context)


 