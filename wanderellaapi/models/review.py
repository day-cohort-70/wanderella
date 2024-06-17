from django.db import models

class Review(models.Model):
    booking = models.ForeignKey(
        "Booking",
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    rating = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)