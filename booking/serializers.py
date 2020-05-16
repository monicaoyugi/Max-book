from rest_framework import serializers
from booking.models import Movie, Tickets, Seats


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class TicketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'


class SeatsSerializer(serializers.ModelSerializer):
    class Mata:
        model = Seats
        fields = '__all__'
