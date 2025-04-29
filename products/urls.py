from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products',ProductViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
]