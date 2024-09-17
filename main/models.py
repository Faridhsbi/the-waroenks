from django.db import models
import uuid 

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)


