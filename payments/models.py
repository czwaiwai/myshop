from django.db import models


# Create your models here.
class Payment(models.Model):
    PAYMENT_STATUS = (
        ("pending", "待支付"),
        ("paying", "支付中"),
        ("paid", "已支付"),
        ("failed", "支付失败"),
        ("refunding", "退款中"),
        ("refunded", "已退款"),
    )
    PAYMENT_METHOD = (
        ("alipay", "支付宝"),
        ("wechat", "微信"),
    )
    order = models.OneToOneField(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="payment",
        verbose_name="订单",
    )
    payment_no = models.CharField(max_length=20, unique=True, verbose_name="支付单号")
    transaction_no = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="交易单号"
    )  # 支付宝或微信的交易单号
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD, verbose_name="支付方式"
    )
    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="pending",
        verbose_name="支付状态",
    )
    fee = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="手续费")
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="支付金额"
    )
    currency = models.CharField(max_length=10, default="CNY", verbose_name="货币")
    client_ip = models.CharField(max_length=20, verbose_name="客户端IP")
    paid_at = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "ms_payment"
        verbose_name = "支付"
        verbose_name_plural = verbose_name
        ordering = ["-create_at"]

    def __str__(self):
        return self.order.order_number


class Refund(models.Model):
    REFUND_STATUS = (
        ("pending", "待退款"),
        ("refunding", "退款中"),
        ("refunded", "已退款"),
        ("failed", "退款失败"),
    )
    payment = models.OneToOneField(
        Payment, on_delete=models.CASCADE, related_name="refund", verbose_name="支付"
    )
    refund_no = models.CharField(max_length=20, unique=True, verbose_name="退款单号")
    transaction_no = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="交易单号"
    )  # 支付宝或微信的交易单号
    refund_status = models.CharField(
        max_length=20, choices=REFUND_STATUS, default="pending", verbose_name="退款状态"
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="退款金额"
    )
    reason = models.CharField(max_length=200, verbose_name="退款原因")
    currency = models.CharField(max_length=10, default="CNY", verbose_name="货币")
    refunded_at = models.DateTimeField(null=True, blank=True, verbose_name="退款时间")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    faild_reason = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="退款失败原因"
    )  # 退款失败原因

    class Meta:
        db_table = "ms_refund"
        verbose_name = "退款"
        verbose_name_plural = verbose_name
        ordering = ["-create_at"]

    def __str__(self):
        return self.refund_no


class PaymentLog(models.Model):
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, related_name="logs", verbose_name="支付"
    )
    action = models.CharField(max_length=20, verbose_name="操作")
    request = models.TextField(verbose_name="请求")
    response = models.TextField(verbose_name="响应")
    success = models.BooleanField(default=False, verbose_name="是否成功")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "ms_payment_log"
        verbose_name = "支付日志"
        verbose_name_plural = verbose_name
        ordering = ["-create_at"]

    def __str__(self):
        return self.message
