from django.db import models
from django.utils import timezone
from django.utils.text import slugify #makes URL-friendly  slugs


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField('Category', related_name="products", blank = True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) #generates slug from product name
        self.available = self.stock > 0
        super(). save(*args, **kwargs)    

    def is_in_stock(self): #checks the stock
        return self.stock > 0
    def is_out_of_stock(self):
        return self.stock == 0
    
    def deduct_stock(self, quantity=1):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
            if self.stock == 0:
                print(f"ALERT: {self.name} is OUT OF STOCK")
            else:
                raise ValueError (f"Not enough stock for {self.name}")

    def add_stock(self, quantity=1): #add stock when over
        self.stock += quantity
        self.save()
        print(f"{quantity} units of {self.name} added. New stock: {self.stock}")

    @classmethod #filters products
    def available_products(cls): #for all products in stock
        return cls.objects.filter(stock__gt=0)
    
    @classmethod
    def out_of_stock_products(cls):
        return cls.objects.filter(stock = 0)
    



# Create your models here.
