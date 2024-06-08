from django.shortcuts import render, redirect
# we import the NewUserForm
from .forms import NewUserForm
# Create your views here.

# register
def register(request):
    if request.method =='POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('myapp/products')
    # create an object or instance of NewUserForm
    form = NewUserForm()
    context={
        'form':form,
    }
   
    return render(request,'users/register.html',context)
