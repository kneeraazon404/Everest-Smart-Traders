from django.shortcuts import render
from .models import ContactPage, Product
from django.shortcuts import get_object_or_404, render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_detail.html", {"product": product})


def about(request):
    return render(request, "about.html")


def landing(request):
    return render(request, "landing.html")


def contact(request):
    contacts = ContactPage.objects.all()
    context = {"contacts": contacts}
    return render(request, "contact.html", context)
