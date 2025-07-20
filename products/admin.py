from django.contrib import admin
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin
from .models import (
    Product,
    Brand,
    Category,
    ProductImage,
    ProductDetail,
    ProductSKU,
    ProductAttribute,
    ProductAttributeValue,
)

# Register your models here.


class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ("name", "parent", "level", "create_at", "update_at")
    list_filter = ("parent", "level")
    search_fields = ("name",)


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "logo_preview", "first_letter")
    list_filter = ("name",)
    search_fields = ("name", "first_letter")
    def logo_preview(self, obj):
        if obj.logo is None:
            return "--"
        return format_html('<img src="/{}" alt="{}" width="80" height="80" />', obj.logo, obj.logo)
    logo_preview.short_description = "Logo"

class ProcutImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductDetailInline(admin.StackedInline):
    model = ProductDetail
    max_num = 1
    can_delete = False


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "brand",
        "sales",
        "stock",
        "price",
        "origin_price",
        "update_at",
    )
    list_filter = ("price",)
    search_fields = ("name", "category")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "category",
                    "brand",
                    "stock",
                    "price",
                    "origin_price",
                ),
            },
        ),
    )
    inlines = [ProcutImageInline, ProductDetailInline]


class ProductSKUAdmin(admin.ModelAdmin):
    list_display = ("sku_code", "product", "price", "stock", "create_at", "update_at")
    search_fields = ("sku_code", "product__name")
    list_filter = ("product",)



class ProductAttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 0

@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ("name", "attribute_value", "create_at", "update_at")
    search_fields = ("name",)

    def attribute_value(self, obj):
        values = obj.values.all()
        if values:
           return ",".join([item.value for item in values])
        return " -- "
    inlines = [ProductAttributeValueInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductSKU, ProductSKUAdmin)
