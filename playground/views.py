from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Order


def say_hello(request):
    queryset = Product.objects.values('id', 'title', 'collection__title')
    # queryset = Product.objects.order_by('unit_price', '-title').reverse()
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # Products: inventory < 10 AND price < 20
    # queryset = Product.objects.filter(
        # Q(inventory__lt=10) | Q(unit_price__lt=20))
    # 'gt' is greater than
    # queryset = Product.objects.filter(unit_price__gt=20)
    # queryset = Product.objects.filter(inventory__lt=10)
    # queryset = Customer.objects.filter(email__icontains='.com')
    # queryset = Order.objects.filter(customer__id=1)
    # exists = Product.objects.get(pk=0).exists()
    #  query_set.filter().filter().order_by()
    #  above filters from objects.all
    
    return render(request, 'hello.html', {'name': 'Louy', 'product': (queryset)})
    # slice element for first 5 operators = 'query_set[0:5]'
    # for product in query_set:
        # print(product)
        # print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    
    
