from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from . import models, permissions, serializers


class ProductViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated] built in
    permission_classes = [permissions.AdminOrReadOnly] # custom
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
   
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewerOrReadOnly]
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializer
   
   
