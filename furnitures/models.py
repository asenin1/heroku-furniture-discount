from django.db import models
from django.core.validators import MinValueValidator
from accounts.models import ProfileUser


class Furniture(models.Model):
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)
    model = models.CharField(max_length=200)
    description = models.TextField()
    discounted_price = models.PositiveIntegerField(validators=[MinValueValidator(10)])
    discount_code = models.CharField(max_length=200)
    image_url = models.URLField()

    def __str__(self):
        return f"Model: {self.model} sold by {self.user}"
