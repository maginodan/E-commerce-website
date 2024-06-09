from django.shortcuts import render, redirect
# we import the NewUserForm
from .forms import NewUserForm
# import login required decorator
from django.contrib.auth.decorators import login_required
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

# profile view with login reqired decorator
@login_required
def profile(request):
    return render(request,'users/profile.html')
