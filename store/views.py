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
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, is_complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {
        'page_title': page_title,
        'items': items,
        'order': order,
    }
    return render(request, 'store/cart.html', context)


def checkout(request):
    page_title = 'Оплата — Інтернет-магазин Дмитра Гурського'
    context = {
        'page_title': page_title
    }
    return render(request, 'store/checkout.html', context)
