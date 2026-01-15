from django.db import models
from django.core.exceptions import ValidationError



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True)

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories'
    )

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} → {self.name}"
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=150, default="", null=True, blank=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True,blank=True)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    thickness = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock = models.PositiveIntegerField(default=0, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.category:
            if self.category.subcategories.exists():
                raise ValidationError({
                    "category": "You must select a sub-category or a category without sub-categories."
                })


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
