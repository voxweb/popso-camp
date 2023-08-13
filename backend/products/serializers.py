from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "store",
            "offer_id",
            "name",
        )

    store = serializers.CharField()
    offer_id = serializers.CharField()
    name = serializers.CharField()