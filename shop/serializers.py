from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price',
                  'in_stock', 'manufacture_date')
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True},
            'price': {'required': True},
            'in_stock': {'required': True}

        }


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):  # Optional
    class Meta:
        model = Product
        fields = '__all__'


class OrderItemCreateSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(required=True)
    quantity = serializers.IntegerField(required=True, min_value=1)


class OrderCreateSerializer(serializers.Serializer):
    order_items = OrderItemCreateSerializer(many=True)

    def validate_order_items(self, value):
        if not value:
            raise serializers.ValidationError(
                "You must include at least one item in your order.")
        product_ids = [item['product_id'] for item in value]
        if len(product_ids) != len(set(product_ids)):
            raise serializers.ValidationError(
                "Duplicate product IDs in order items.")
        for item_data in value:
            try:
                product = Product.objects.get(id=item_data['product_id'])
                if not product.in_stock:
                    raise serializers.ValidationError(
                        f"Product with ID {product.id} ('{product.name}') is out of stock.")
            except Product.DoesNotExist:
                pass  # handling above
        return value

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        user = self.context['request'].user
        order = Order.objects.create(user=user)
        for item_data in order_items_data:
            product = Product.objects.get(id=item_data['product_id'])
            quantity = item_data['quantity']
            OrderItem.objects.create(
                order=order, product=product, quantity=quantity)
        return order


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField(
        source='product.name', read_only=True)  # Display product name

    class Meta:
        model = OrderItem
        fields = ('product', 'quantity', 'total_price')
        read_only_fields = ('total_price',)


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.CharField(
        source='user.username', read_only=True)  # Display username

    class Meta:
        model = Order
        fields = ('id', 'user', 'order_time', 'status', 'order_items')
        read_only_fields = ('id', 'user', 'order_time', 'status')
