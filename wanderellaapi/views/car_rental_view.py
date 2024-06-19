from wanderellaapi.models import RentalCar
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


# Generate a ViewSet class for car rentals based on the RentalCar model. The class should have the following methods: get, list, update, destroy, create
class RentalCarView(ViewSet):

    # List method
    def list(self, request):
        cars = RentalCar.objects.all()
        serialized = RentalCarSerializer(cars, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    # Retrieve method
    def retrieve(self, request, pk=None):
        car = RentalCar.objects.get(pk=pk)
        serialized = RentalCarSerializer(car, many=False)
        return Response(serialized.data, status=status.HTTP_200_OK)

    # Create method
    def create(self, request):
        car_type = request.data.get('car_type', None)
        make = request.data.get('make', None)
        model = request.data.get('model', None)
        year = request.data.get('year', None)
        price_per_day = request.data.get('price_per_day', None)

        if car_type is None or make is None or model is None or year is None or price_per_day is None:
            return Response({'message': 'You must provide the "car_type", "make", "model", "year", and "price_per_day" properties in your JSON'}, status=status.HTTP_400_BAD_REQUEST)

        new_car = RentalCar()
        new_car.car_type = car_type
        new_car.make = make
        new_car.model = model
        new_car.year = year
        new_car.price_per_day = price_per_day
        new_car.save()

        serialized_car = RentalCarSerializer(new_car, many=False)

        return Response(serialized_car.data, status=status.HTTP_201_CREATED)

    # Update method
    def update(self, request, pk=None):
        car_type = request.data.get('car_type', None)
        make = request.data.get('make', None)
        model = request.data.get('model', None)
        year = request.data.get('year', None)
        price_per_day = request.data.get('price_per_day', None)

        if car_type is None or make is None or model is None or year is None or price_per_day is None:
            return Response({'message': 'You must provide the "car_type", "make", "model", "year", and "price_per_day" properties in your JSON'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            car = RentalCar.objects.get(pk=pk)
            car.car_type = car_type
            car.make = make
            car.model = model
            car.year = year
            car.price_per_day = price_per_day
            car.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except RentalCar.DoesNotExist:
            return Response({'message': 'The car you requested does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # Destroy method
    def destroy(self, request, pk=None):
        try:
            car = RentalCar.objects.get(pk=pk)
            car.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except RentalCar.DoesNotExist:
            return Response({'message': 'The car you requested does not exist'}, status=status.HTTP_404_NOT_FOUND)

# Rental car serializer
class RentalCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentalCar
        fields = ('id', 'car_type', 'make', 'model', 'year', 'price_per_day',)

