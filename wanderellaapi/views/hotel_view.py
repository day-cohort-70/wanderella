from wanderellaapi.models import Hotel, Amenity
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

class HotelView(ViewSet):

    def retrieve(self, request, pk=None):
        hotel = Hotel.objects.get(pk=pk)
        serialized = HotelSerializer(hotel, many=False)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        search_city = request.query_params.get('city', None)

        # Start off assuming I want all hotels
        hotels = Hotel.objects.all()

        # Did the client use the `city` query string parameter?
        if search_city is not None:
            hotels = hotels.filter(city=search_city)

        serialized = HotelSerializer(hotels, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class HotelAmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Amenity
        fields = ( 'id', 'name', )


class HotelSerializer(serializers.ModelSerializer):
    amenities = HotelAmenitySerializer(many=True)

    class Meta:
        model = Hotel
        fields = ( 'id', 'name', 'address', 'city', 'amenities', )