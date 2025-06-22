from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name="手机号")
    avator = models.ImageField(upload_to="avatar", verbose_name="头像")
    score = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="积分")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    # 解决 groups 字段的反向访问器冲突
    groups = models.ManyToManyField(
        Group,
        verbose_name=("groups"),
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="user_set_ms_groups",  # 修改为唯一的名称
        related_query_name="user_ms",
    )
    # 解决 user_permissions 字段的反向访问器冲突
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=("user permissions"),
        blank=True,
        help_text=("Specific permissions for this user."),
        related_name="user_set_ms_permissions",  # 修改为唯一的名称
        related_query_name="user_ms",
    )

    class Meta:
        db_table = "ms_users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class Address(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="addresses", verbose_name="用户"
    )
    title = models.CharField(max_length=20, verbose_name="地址名称")
    contact_name = models.CharField(max_length=20, verbose_name="收货人")
    contact_phone = models.CharField(max_length=11, verbose_name="联系电话")
    province = models.CharField(max_length=20, verbose_name="省")
    city = models.CharField(max_length=20, verbose_name="市")
    district = models.CharField(max_length=20, verbose_name="区")
    place = models.CharField(max_length=50, verbose_name="详细地址")
    email = models.CharField(
        max_length=30, null=True, blank=True, verbose_name="电子邮箱"
    )
    is_default = models.BooleanField(default=False, verbose_name="默认地址")
    is_deleted = models.BooleanField(default=False, verbose_name="逻辑删除")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "ms_address"
        verbose_name = "用户地址"
        verbose_name_plural = verbose_name
        ordering = ["-update_at"]
