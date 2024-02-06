from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product


def say_hello(request):
    # 'gt' is greater than
    # queryset = Product.objects.filter(unit_price__gt=20)
    queryset = Product.objects.filter(title__icontains='coffee')
    # exists = Product.objects.get(pk=0).exists()
    #  query_set.filter().filter().order_by()
    #  above filters from objects.all
    
    return render(request, 'hello.html', {'name': 'Louy', 'products': list(queryset)})
    # slice element for first 5 operators = 'query_set[0:5]'
    # for product in query_set:
        # print(product)
        # print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    
    
