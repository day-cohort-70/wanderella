from wanderellaapi.models import Airline
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class AirlineView(ViewSet):

    def retrieve(self, request, pk=None):
        try:
            airline = Airline.objects.get(pk=pk)
            serialized = AirlineSerializer(airline, many=False)
            return Response(serialized.data, status=status.HTTP_200_OK)

        except Airline.DoesNotExist:
            return Response({'message': 'The airline you requested does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def list(self, request):
        cities = Airline.objects.all()
        serialized = AirlineSerializer(cities, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        # Extract fields from client request body
        name = request.data.get('name', None)
        iata = request.data.get('iata_code', None)

        if iata is None or name is None:
            return Response({'message': 'You must provide the "name" and "iata_code" properties in your JSON'}, status=status.HTTP_400_BAD_REQUEST)

        # Create an instance of needed model, and set properties
        new_airline = Airline()
        new_airline.name = name
        new_airline.iata_code = iata
        new_airline.save()

        # Serialize the newly created airline
        serialized_airline = AirlineSerializer(new_airline, many=False)

        # Send data back in a response, with 201 status code
        return Response(serialized_airline.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        # Extract fields from client request body
        name = request.data.get('name', None)
        iata = request.data.get('iata_code', None)

        if iata is None or name is None:
            return Response({'message': 'You must provide the "name" and "iata_code" properties in your JSON'}, status=status.HTTP_400_BAD_REQUEST)

        # Update existing row in database
        try:
            requested_airline = Airline.objects.get(pk=pk)
            requested_airline.name = name
            requested_airline.iata_code = iata
            requested_airline.save()

            # Send data back in a response, with 204 status code
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Airline.DoesNotExist:
            return Response({'message': 'The airline you requested does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def destroy(self, request, pk):
        try:
            airline_to_destroy = Airline.objects.get(pk=pk)
            airline_to_destroy.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Airline.DoesNotExist:
            return Response({'message': 'The airline you requested does not exist'}, status=status.HTTP_404_NOT_FOUND)


class AirlineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Airline
        fields = ('id', 'name', 'iata_code',)