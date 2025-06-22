from django.db import models


# Create your models here.
class Coupon(models.Model):
    COUPON_TYPE = (("percent", "百分比折扣"), ("fixed", "固定金额折扣"))

    name = models.CharField(max_length=100, verbose_name="优惠名称")
    code = models.CharField(max_length=100, unique=True, verbose_name="优惠码")
    type = models.CharField(
        max_length=100, choices=COUPON_TYPE, verbose_name="优惠类型"
    )
    discount_value = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="优惠值"
    )
    min_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="最低消费"
    )
    max_uses = models.IntegerField(default=1, verbose_name="最大使用次数")
    users_count = models.IntegerField(default=0, verbose_name="用户数量")
    start_date = models.DateTimeField(verbose_name="开始时间")
    end_date = models.DateTimeField(verbose_name="结束时间")
    active = models.BooleanField(default=True, verbose_name="是否激活")

    def __str__(self):
        return self.name


class UserCoupon(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name="用户"
    )
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, verbose_name="优惠券")
    used = models.BooleanField(default=False, verbose_name="是否使用")
    used_at = models.DateTimeField(null=True, blank=True, verbose_name="使用时间")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return f"{self.user.username} - {self.coupon.name}"
