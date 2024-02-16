from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Average, Sum
from django.db.models import Q, F, Values, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, OrderItem


def say_hello(request):
    discounted_price = ExpressionWrapper(
        F('unit_price') * 0.8, output_field=DecimalField())
    
    queryset = Customer.objects.annotate(
        discounted_price=discounted_price
    )
    
    queryset = Customer.objects.annotate(
        full_name=Concat('first_name', Value(' '), 
                    'last_name')
    )
    
    
    # How many orders?
    result = Order.objects.aggregate(count=Count('id'))
    
    #How many units of product have been sold?
    result = OrderItem.objects.filter(product__id=1).aggregate(
        units_sold=Sum('quantity'))
    
    # How many orders has one customer placed?
    result = Order.objects.filter('customer__id=1').aggregate(count=Count('id'))
    
    # What is the average, min, and max price of products in collection 1?
    result =- Product.objects.filter(collection__id=3).aggregate(
        min_price=Min('unit_price'),
        avg_price=Avg('unit_price'),
        max_price=Max('unit_price'),
    )
    
    queryset = Order.objects.select_related('customer').prefetch_related(
        'orderitem_set__product').order_by('-placed_at')[: 5]
    queryset = Product.objects.filter(
        id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    queryset = Product.objects.prefetch_related('promotions').select_related('collection')
   
    
    return render(request, 'hello.html', {'name': 'Louy', 'result': list(queryset)})
    # slice element for first 5 operators = 'query_set[0:5]'
    # for product in query_set:
        # print(product)
        # print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    
    
