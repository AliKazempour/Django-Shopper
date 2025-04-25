from django.contrib import admin
from .models import Product, Order, OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'in_stock', 'manufacture_date')
    search_fields = ('name',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'total_price')
    search_fields = ('order__id', 'product__name')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_time', 'status')
    list_filter = ('status',)
    search_fields = ('user__username',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
