from django.db import models

class Amenity(models.Model):
    # Database yes
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Database no
    hotels = models.ManyToManyField(
        "Hotel",
        through="HotelAmenity",
        related_name="amenities"
    )
