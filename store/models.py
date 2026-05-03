from django.db import models

class Product(models.Model):
    """
    Represents a product in the store application.
    
    Attributes:
        name (str): Name of the product
        price (decimal): Price of the product
        description (str): Product details
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        """Returns the string representation of the product."""
        return self.name
