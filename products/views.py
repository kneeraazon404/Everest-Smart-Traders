from django.shortcuts import render
from .models import ContactPage, Product
from django.shortcuts import get_object_or_404, render
from .models import Product
from django.core.paginator import Paginator


def product_list(request):

    products_list = Product.objects.all()

    paginator = Paginator(products_list, 8)

    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    return render(request, "product_list.html", {"products": products})


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
