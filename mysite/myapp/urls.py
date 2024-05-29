
from django.contrib import admin
from django.urls import path
# from myapp import views
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index),
    path('products/',views.products),
    path('products/<int:id>/', views.product_detail),
]
