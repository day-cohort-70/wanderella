from django.db import models

class Flight(models.Model):
    airline = models.ForeignKey(
        "Airline",
        on_delete=models.CASCADE,
        related_name="flights"
    )
    flight_number = models.CharField(max_length=20)
    departure_airport = models.CharField(max_length=20)
    arrival_airport = models.CharField(max_length=20)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)