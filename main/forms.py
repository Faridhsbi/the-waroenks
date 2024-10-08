from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "description", "price", "stock", "rating"]

    def clean_product(self):
        product = self.cleaned_data["product_name"]
        return strip_tags(product)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)