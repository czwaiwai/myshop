from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# 分类
class Category(MPTTModel):
    name = models.CharField(max_length=10, verbose_name="类别名称")
    desc = models.CharField(
        max_length=30, default=None, null=True, blank=True, verbose_name="类别详情"
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        db_index=True,
        verbose_name="父级类别",
    )
    attributes = models.ManyToManyField(
        "ProductAttribute",
        blank=True,
        verbose_name="允许的SKU属性",
        related_name="categories",
    )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        db_table = "ms_category"
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 品牌
class Brand(models.Model):
    name = models.CharField(max_length=20, verbose_name="品牌名称")
    logo = models.ImageField(
        upload_to="brand", default=None, blank=True, null=True, verbose_name="品牌logo"
    )
    first_letter = models.CharField(max_length=1, verbose_name="品牌首字母")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "ms_brand"
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name="商品名称")
    category = TreeForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="商品类别",
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="商品品牌",
    )
    sales = models.IntegerField(default=0, verbose_name="商品销量")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="商品价格"
    )
    origin_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="商品原价"
    )
    stock = models.IntegerField(default=0, verbose_name="商品库存")
    is_active = models.BooleanField(default=True, verbose_name="商品状态")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "ms_product"
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images", verbose_name="商品"
    )
    image = models.ImageField(upload_to="product", verbose_name="商品图片")
    order = models.IntegerField(default=0, verbose_name="图片顺序")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "ms_product_image"
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name
        ordering = ["order"]

    def __str__(self):
        return self.product.name


class ProductDetail(models.Model):
    product = models.OneToOneField(
        Product, on_delete=models.CASCADE, related_name="detail", verbose_name="商品"
    )
    content = models.TextField(verbose_name="商品详情")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "ms_product_detail"
        verbose_name = "商品详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return ""


class ProductAttribute(models.Model):
    name = models.CharField(max_length=20, verbose_name="属性名称")
    desc = models.CharField(max_length=50, default=None, blank=True, null=True, verbose_name="属性解释")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "ms_product_attribute"
        verbose_name = "商品属性"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.desc} - {self.name}"

class ProductAttributeValue(models.Model):
    attribute = models.ForeignKey(
        "ProductAttribute",
        on_delete=models.CASCADE,
        related_name="values",
        verbose_name="属性",
    )
    value = models.CharField(max_length=20, verbose_name="属性值")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "ms_product_attribute_value"
        verbose_name = "商品属性值"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value


class ProductSKU(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="skus", verbose_name="商品"
    )
    sku_name = models.CharField(max_length=50, verbose_name="SKU名称")
    sku_code = models.CharField(max_length=50, unique=True, verbose_name="SKU Code")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="SKU价格")
    stock = models.PositiveIntegerField(default=0, verbose_name="SKU库存")
    attributes = models.ManyToManyField(
        "ProductAttributeValue",
        related_name="attribute_skus",
        verbose_name="SKU属性",
    )
    is_active = models.BooleanField(default=True, verbose_name="SKU状态")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "ms_product_sku"
        verbose_name = "商品SKU"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.product}-{self.sku_code}"
