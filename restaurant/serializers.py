from rest_framework.serializers import ModelSerializer
from .models import Booking, MenuItem


class MenuSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["title", "price", "inventory"]


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
