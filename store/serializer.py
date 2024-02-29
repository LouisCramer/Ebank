from rest_framework import serializer

class ProductSerializer(serializer.Serializer):
    id = serializers.IntegerField()
    title = serializer.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=2, decimal_places=2)
    