from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=150, default="", null=True, blank=True)
    brands = {
        "Kastamonu Entegre" :  "Kastamonu Entegre",
        "Starwood"  : "Starwood",
        "Swiss Krono" : "Swiss Krono"
    }
    brand = models.CharField(max_length=200, choices=brands, null=True, blank=True, default="Kastamonu Entegre")
    width = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    thickness = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    surfaces = {
        "Soft Touch" : "Soft Touch",
        "Glossy" : "Glossy"
    }
    surface = models.CharField(max_length=200, choices=surfaces, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock = models.PositiveIntegerField(default=0, null=False, blank=False)
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
