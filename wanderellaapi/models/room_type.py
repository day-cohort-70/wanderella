from django.db import models

class RoomType(models.Model):
    hotel = models.ForeignKey("Hotel", on_delete=models.CASCADE, related_name="room_types")
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)