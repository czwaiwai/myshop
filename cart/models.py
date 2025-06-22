from django.db import models

# Create your models here.
class Card(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE, related_name='cart', verbose_name='用户')

class CardItem(models.Model):
    cart = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='items', verbose_name='购物车')
    sku = models.ForeignKey('products.ProductSKU', on_delete=models.CASCADE, related_name='cart_items', verbose_name='商品SKU')
    quantity = models.IntegerField(default=1, verbose_name='数量')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'ms_cart_item'
        verbose_name = '购物车商品'
        verbose_name_plural = verbose_name
        ordering = ['-update_at']

    def __str__(self):
        return self.sku.sku_name