from django.shortcuts import render
from .models import Product

def home(request):
    """
    Displays all products.
    """
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})
