from django.db import models

class Airline(models.Model):
    name = models.CharField(max_length=255)
    iata_code = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)