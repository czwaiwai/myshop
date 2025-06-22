from django.db import models

# Create your models here.
class Order(models.Model):
    ORDER_STATUS = (
        ('pending', '待支付'), 
        ('paid', '已支付'), 
        ('shipping', '发货中'),
        ('delivered', '已送达'),
        ('completed', '已完成'), 
        ('cancelled', '已取消'),
    )
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='orders', verbose_name='用户')
    ordrer_number = models.CharField(max_length=20, unique=True, verbose_name='订单号')
    address = models.ForeignKey('users.Address', on_delete=models.CASCADE, related_name='orders', verbose_name='地址')
    status = models.CharField(max_length=20, choices=ORDER_STATUS, default='pending', verbose_name='订单状态')
    payment_method = models.CharField(max_length=20, verbose_name='支付方式')
    payment_time = models.DateTimeField(null=True, blank=True, verbose_name='支付时间')
    shipping_time = models.DateTimeField(null=True, blank=True, verbose_name='发货时间')
    delivery_time = models.DateTimeField(null=True, blank=True, verbose_name='送达时间')
    completion_time = models.DateTimeField(null=True, blank=True, verbose_name='完成时间')

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='总价')
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='优惠')
    shipping_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='运费')
    final_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='实付金额')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'ms_order'
        verbose_name = '订单'
        verbose_name_plural = verbose_name
        ordering = ['-create_at']

    def __str__(self):
        return self.order_number
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='订单')
    sku = models.ForeignKey('products.ProductSKU', on_delete=models.CASCADE, verbose_name='商品SKU')
    name = models.CharField(max_length=50, verbose_name='商品名称')
    quantity = models.IntegerField(default=1, verbose_name='数量')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')
    sub_total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='总价')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'ms_order_item'
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name
        ordering = ['-create_at']

    def __str__(self):
        return self.sku.sku_name