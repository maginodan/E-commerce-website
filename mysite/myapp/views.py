from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def index(request):
    return HttpResponse("helo world")

def products(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'myapp/index.html',context)
    


