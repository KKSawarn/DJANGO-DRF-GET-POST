from rest_framework import serializers
from .models import Shirt,Category

class CreateShirtSerializer(serializers.ModelSerializer):
    category_id = serializers.CharField(source="category__id")
    class Meta:
        model = Shirt
        fields = (
            "item_id",
            "brand_name",
            "fabric",
            "sku",
            "is_imported",
            "category_id"
        )

class ShirtSerializerParam(serializers.ModelSerializer):
    category = serializers.CharField(source="category__id")
    class Meta:
        model = Shirt
        fields = (
            "item_id",
            "brand_name",
            "fabric",
            "category",
        )

class ShirtDetailSerializer(serializers.ModelSerializer):
    # item_id = serializers.IntegerField(source="id")
    category_id = serializers.CharField(source="category.category_id")
    category_price = serializers.CharField(source="category.price")
    category_size = serializers.CharField(source="category.size")
    class Meta:
        model = Shirt
        fields = (
            "item_id",
            "brand_name",
            "fabric",
            "is_imported",
            "category_id",
            "category_price",
            "category_size",
        )

class CreateCategorySerializer(serializers.ModelSerializer):
    category_id = serializers.IntegerField()
    size = serializers.CharField(max_length=10)
    price = serializers.DecimalField(max_digits=19, decimal_places=2)
    class Meta:
        model = Category
        fields = (
            "category_id",
            "size",
            "price",
        )

class CategorySerializerParam(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "size",
            "price"
        )

class CategoryDetailSerializer(serializers.ModelSerializer):
    model = Category
    fields = (
        "category_id",
        "size",
        "price",
    )

    




