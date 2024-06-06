from django.shortcuts import render
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

def add_product(request):
    if request.method =='POST':
    #variable                 name and id passed
       name = request.POST.get('name')
       price = request.POST.get('price')
       desc = request.POST.get('desc')
       image = request.FILES['upload']
    return render(request,'myapp/addproduct.html')

 