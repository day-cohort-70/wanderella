from wanderellaapi.models import Flight
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class FlightView(ViewSet):

    def retrieve(self, request, pk=None):
        flight = Flight.objects.get(pk=pk)
        serialized = FlightSerializer(flight, many=False)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        cities = Flight.objects.all()
        serialized = FlightSerializer(cities, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ('id', 'airline',
                  'flight_number', 'departure_airport', 'arrival_airport',
                  'departure_time', 'arrival_time',)