from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    depth = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock = models.PositiveIntegerField(default=0, null=False, blank=False)

    colors = {
        "Red": "red",
        "Green": "green",
        "Blue": "blue",
        "White": "White",
        "Black": "black",
        "Grey": "grey",
        "Yellow": "yellow",
        "Brown": "brown",
        "Beige": "beige"
    }

    color = models.CharField(max_length=200, choices=colors, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.name


class Work(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='our_works/', blank=True, null=True)

    def __str__(self):
        return self.name
