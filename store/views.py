from django.shortcuts import render

from store.models import *


def home(request):
    page_title = 'Головна — Інтернет-магазин Дмитра Гурського'
    products = Product.objects.all()
    context = {
        'page_title': page_title,
        'products': products
    }

    return render(request, 'store/home.html', context)


def cart(request):
    page_title = 'Корзина — Інтернет-магазин Дмитра Гурського'
    context = {
        'page_title': page_title
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    page_title = 'Оплата — Інтернет-магазин Дмитра Гурського'
    context = {
        'page_title': page_title
    }
    return render(request, 'store/checkout.html', context)
