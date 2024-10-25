from django.shortcuts import render
from .models import Product


# Create your views here.
def index(req):
    all_products = Product.objects.all()
    return render(req,'index.html',{'products':all_products})
