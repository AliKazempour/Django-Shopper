from django.urls import path
from .views import (ProductCreateView,
                    ProductListView, ProductDetailView, OrderCreateView, OrderListView,)


urlpatterns = [
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/', OrderListView.as_view(), name='order-list'),
]
