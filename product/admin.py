from django.contrib import admin
from .models import Product, ProductCategory, ProductDetail
# Register your models here.

class ProductDetailInline(admin.TabularInline):
    model = ProductDetail
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "short_description", "color"]
    list_filter = ["product_category"]
    search_fields = ["name"]
    inlines = [ProductDetailInline]

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ["product_id", "serial_number", "is_sold"]
    list_filter = ["is_sold"]
    search_fields = ["product_id"]
    fields = ["serial_number", "cost", "product_id"]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
admin.site.register(ProductDetail, ProductDetailAdmin)