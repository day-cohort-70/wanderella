from wanderellaapi.models import Booking, Flight, RentalCar, Hotel, UserProfile
from rest_framework import serializers, status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class BookingView(ViewSet):

    def create(self, request):
        hotel = request.data.get('hotelId', None)
        flight = request.data.get('flightId', None)
        car = request.data.get('carId', None)
        price = request.data.get('price', None)
        book_date = request.data.get('bookingDate', None)

        if hotel is None or flight is None or car is None or price is None or book_date is None:
            return Response(
                {'message': 'You must provide all required keys in the JSON body'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            new_booking = Booking()
            new_booking.customer = UserProfile.objects.get(user=request.auth.user)
            new_booking.hotel = Hotel.objects.get(pk=hotel)
            new_booking.flight = Flight.objects.get(pk=flight)
            new_booking.rental_car = RentalCar.objects.get(pk=car)
            new_booking.booking_date = book_date
            new_booking.total_price = price
            new_booking.save()

        except (Hotel.DoesNotExist, Flight.DoesNotExist, RentalCar.DoesNotExist):
            return Response(
                {'message': 'You provided an invalid `id` for the hotel, or flight, or car'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serialized_booking = BookingSerializer(new_booking, many=False)

        return Response(serialized_booking.data, status=status.HTTP_201_CREATED)


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ('id', 'hotel', 'flight', 'rental_car', 'booking_date', 'total_price', )