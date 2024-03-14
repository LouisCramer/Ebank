from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.db.models.aggregates import Count, Max, Min, Sum
from django.db.models import Q, F, Func, ExpressionWrapper
# from django.db.models.functions import Concat, transaction
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from store.models import Product, Customer, OrderItem
from tags.models import TaggedItem



def say_hello(request):
   
    # extracting data with advanced querying
    with connection.cursor() as cursor:
        cursor.callproc('get_customers', [1, 2, 'a'])

    # extracting raw SQL the basic way
    queryset = Product.objects.raw('SELECT id, title FROM store_product')
    
    with transaction.atomic():
        order = Order()
        order.customer_id = 1
        order.save()
        
        item = OrderItem()
        item.order = order
        item.product_id = 1
        item.quantity = 1
        item.unit_price = 10
        item.save()
    
    # Creating item in cart
    cart = Cart
    cart.save()
    
    Mustard = CartItem()
    Mustard.cart = cart
    Mustard.product_id = 1
    Mustard.quantity = 1
    Mustard.save()
    
    # updating item in cart
    Mustard = CartItem.objects.get(pk=1)
    Mustard.quantity = 2
    Mustard.save()
    
    # Deleting item from cart
    cart = Cart(pk=1)
    cart.delete()
    
    collection = Collection.get(pk=11)
    collection.delete()
    
    Collection.objects.filter(id_gt=5).delete()
    
    
    # Collection.objects.filter(pk=11).update(featured_product=None)
    
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
    # result = Order.objects.aggregate(count=Count('id'))
    
    # #How many units of product have been sold?
    # result = OrderItem.objects.filter(product__id=1).aggregate(
    #     units_sold=Sum('quantity'))
    
    # # How many orders has one customer placed?
    # result = Order.objects.filter('customer__id=1').aggregate(count=Count('id'))
    
    # # What is the average, min, and max price of products in collection 1?
    # result =- Product.objects.filter(collection__id=3).aggregate(
    #     min_price=Min('unit_price'),
    #     avg_price=Avg('unit_price'),
    #     max_price=Max('unit_price'),
    # )
    
    # queryset = Order.objects.select_related('customer').prefetch_related(
    #     'orderitem_set__product').order_by('-placed_at')[: 5]
    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # queryset = Product.objects.prefetch_related('promotions').select_related('collection')
   
    
    return render(request, 'hello.html', {'name': 'Louy', 'tags': list(queryset)})
    # slice element for first 5 operators = 'query_set[0:5]'
    # for product in query_set:
        # print(product)
        # print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    
    
