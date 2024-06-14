from django.db import models

class HotelAmenity(models.Model):
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE)
    amenity = models.ForeignKey("Amenity", on_delete=models.CASCADE)