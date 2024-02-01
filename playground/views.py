from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    query_set = Product.objects.all()
    
    for product in query_set:
        print(product)
        print("IP Address for debug-toolbar: " + request.META['REMOTE_ADDR'])
    
    return render(request, 'hello.html', {'name': 'Louy'})
