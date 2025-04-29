from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import AllowAny

from django.shortcuts import render
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


def product_list(request):
    products = Product.objects.all()
    print("Productfetched",products)
    return render(request, 'product_list.html', {'products': products})

