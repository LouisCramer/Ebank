from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Average, Sum
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, OrderItem


def say_hello(request):
    result = Product.objects.aggregate(Count('id'))
    
    queryset = Order.objects.select_related('customer').prefetch_related(
        'orderitem_set__product').order_by('-placed_at')[: 5]
    queryset = Product.objects.filter(
        id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    queryset = Product.objects.prefetch_related('promotions').select_related('collection')
   
    
    return render(request, 'hello.html', {'name': 'Louy', 'result': result})
    # slice element for first 5 operators = 'query_set[0:5]'
    # for product in query_set:
        # print(product)
        # print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    
    
