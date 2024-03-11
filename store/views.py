from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models.aggregates import Count
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .filters import ProductFilter
from .models import Product, Collection, Review, Cart
from .pagination import DefaultPagination
from .serializer import ProductSerializer, CollectionSerializer, ReviewSerializer, CartSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = DefaultPagination
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']
    
    def get_queryset(self):
        queryset = Product.objects.all()
        collection_id = self.request.query_params.get('collection_id')
        if collection_id is not None:
            queryset = queryset.filter(collection_id=collection_id)
        
        return queryset
    
    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request ):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Product cannot be deleted as it is associated with an order'}),
        
        return super().destroy(request, *args, **kwargs)
   
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(
        products_count=Count('products')).all()
    serializer_class = CollectionSerializer
    
    def destroy(self, request):
        if OrderItem.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'})
        
        return super().destroy(request, *args, **kwargs)
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        queryset = Product.objects.all()
        collection_id = self.request.query_params['collection_id']
        if collection_id is not None:
            queryset = queryset.filter(collection_id=collection_id)
        
    def get_serializer_context(self):
        return Review.objects.filter(product_id=sel.kwargs['product_pk'])
    
    def get_serializer_context(self):
        return { 'product_id': self.kwargs['product_pk']}
    
class CartViewSet(CreateModelMixin, 
                  RetrieveModelMixin, 
                  GenericViewSet, 
                  DestroyModelMixin):
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializer
    

    
    

