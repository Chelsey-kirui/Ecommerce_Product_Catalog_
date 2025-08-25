from django.contrib import admin
from .models import Category, Product


# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'product_count') #provides a list of products
    search_fields = ('name', 'description', 'slug') #allows search by name/ description of the product
    
    def product_count(self, obj): #counts products per category
        return obj.products.count()
    product_count.short_description = 'Products'

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category_list', 'stock_status')
    list_filter = ('categories', 'stock')
    search_fields = ('name', 'description', 'slug')
    
    def stock_status(self, obj):
        return "In Stock" if obj.stock  > 0 else "Out of Stock"
    stock_status.short_description = 'Status'
    
    def category_list(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    category_list.short_description = 'Categories'


# Register your models here.
