from django.shortcuts import render
from django_filters import CharFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from . import models, permissions, serializers


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated] built in
    permission_classes = [permissions.AdminOrReadOnly] # custom
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price']
    
   
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewerOrReadOnly]
    # queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer
    
    # filtering using queryset
    # def get_queryset(self):
    #     queryset = models.ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:
    #         queryset = queryset.filter(user__username__icontains=username) #user = filedname in reviews model, __username = filedname in user model, __icontains = remove case sensitive
    #     return queryset
    
    
    # filtering with django filters
    queryset = models.ProductReview.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user__username', 'product', 'rating']
    ordering_fields = ['rating']
   
   
