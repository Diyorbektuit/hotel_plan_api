from rest_framework import serializers
from .models import Region, Hotel, Order


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class HotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
