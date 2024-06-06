
from django.contrib import admin
from django.urls import path
# from myapp import views
from . import views
app_name ='myapp'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('products/',views.products),
    path('products/<int:id>/', views.product_detail,name='product_detail'),
    path('products/add/', views.add_product,name='add_product'),
] 
