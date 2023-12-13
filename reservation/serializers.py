from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User

class menuSerializer (serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['title', 'price', 'inventory' ]
        
class bookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['name', 'No_of_guests', 'BookingDate' ]
        
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']