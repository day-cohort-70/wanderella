from wanderellaapi.models import Flight, Airline
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class FlightView(ViewSet):

    def retrieve(self, request, pk=None):
        flight = Flight.objects.get(pk=pk)
        serialized = FlightSerializer(flight, many=False)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        chosen_airline = request.query_params.get('airline', None)

        # Did the client use the `airline` query string parameter?
        if chosen_airline is not None:

            # First, get the airline from the database to see if a valid one was requested
            try:
                airline = Airline.objects.get(pk=chosen_airline)
            except Airline.DoesNotExist:
                return Response(
                    {'message': 'You requested flights for a non-existent airline'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Valid airline `id` specified. Filter all flights by that airline.
            flights = Flight.objects.filter(airline=airline)
            serialized = FlightSerializer(flights, many=True)
            return Response(serialized.data, status=status.HTTP_200_OK)

        # Client did NOT specify `airline` query string param, so get all of 'em
        flights = Flight.objects.all()
        serialized = FlightSerializer(flights, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flight
        fields = ('id', 'airline',
                  'flight_number', 'departure_airport', 'arrival_airport',
                  'departure_time', 'arrival_time',)