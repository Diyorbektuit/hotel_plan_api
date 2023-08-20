from rest_framework import generics
from .models import Hotel, Region, Order
from .serializers import HotelSerializers, RegionSerializer, OrderSerializers


class RegionListAPIView(generics.ListAPIView):
    serializer_class = RegionSerializer

    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = Region.objects.all()
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class HotelListAPIView(generics.ListAPIView):
    serializer_class = HotelSerializers

    def get_queryset(self):
        region_id = self.request.GET.get('region_id')
        queryset = Hotel.objects.filter(region_id=region_id)
        return queryset


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
