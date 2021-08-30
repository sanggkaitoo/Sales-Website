from django.shortcuts import render
from store.models import Product
from orders import models as orders
from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context=context)


def dashboard_with_pivot(request):
    return render(request, 'dashboard/dashboard_with_pivot.html', {})


def pivot_data(request):
    all_obj = [*orders.Order.objects.all(), *orders.Payment.objects.all()]
    # dataset = Order.objects.all()
    data = serializers.serialize('json', all_obj)
    return JsonResponse(data, safe=False)
