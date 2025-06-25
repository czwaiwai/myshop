from django.contrib import admin
from .models import Product, Brand, Category, ProductImage, ProductSKU

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "level", "create_at", "update_at")
    list_filter = ("parent", "level")
    search_fields = ("name",)


admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductSKU)
