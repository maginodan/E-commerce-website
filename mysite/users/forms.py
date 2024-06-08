from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# we need to customize and modify the fields in the django form
# create our class and inherit the UserCreationForm
class NewUserForm(UserCreationForm):
    # define the fields we want to display to the user
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'focus:outline-none','placeholder':'johndoe@gmail.com'}))
    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'focus:outline-none','placeholder':'user123'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class':'focus:outline-none'}))

# model
# meta means class which defines a structure of this class instead
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    # saving a user  
    def save(self,commit=True):
        user=super(NewUserForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user      