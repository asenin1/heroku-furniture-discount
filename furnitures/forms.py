from django import forms
from django.core.validators import MinValueValidator
from .models import Furniture


class CreateForm(forms.ModelForm):
    discounted_price = forms.IntegerField(required=True, validators=[MinValueValidator(10)])  # Works

    class Meta:
        model = Furniture
        fields = ('id', 'model', 'description', 'discounted_price', 'discount_code', 'image_url')
