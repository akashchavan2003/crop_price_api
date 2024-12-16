from rest_framework import serializers
from .models import Crop
from decimal import Decimal
class CropSerializer(serializers.ModelSerializer):
    prices = serializers.SerializerMethodField()

    class Meta:
        model = Crop
        fields = '__all__'

    def get_prices(self, obj):
        if obj.base_price is None:
            return None
        prices = {
            'kg': obj.base_price,
            'g': obj.base_price / Decimal('1000'),
            'ton': obj.base_price * Decimal('1000'),
            'lb': obj.base_price * Decimal('2.20462'),
            'quintal': obj.base_price * Decimal('100'),
        }
        return prices

class CropPriceConversionSerializer(serializers.Serializer):
    unit = serializers.CharField(max_length=20)
    converted_price = serializers.SerializerMethodField()

    def get_converted_price(self, obj):
        unit = self.initial_data.get('unit', 'kg')
        if unit == 'grams':
            return obj.base_price / 1000
        elif unit == 'tons':
            return obj.base_price * 1000
        return obj.base_price