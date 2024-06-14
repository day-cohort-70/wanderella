from django.db import models

class Booking(models.Model):
    customer = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    flight = models.ForeignKey("Flight", on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE, null=True, blank=True)
    rental_car = models.ForeignKey("RentalCar", on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)