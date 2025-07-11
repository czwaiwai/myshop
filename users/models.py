from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from .managers import MsUserManager


class UserType(models.TextChoices):
    CLIENT = "client", "普通用户"
    MANAGER = "manager", "后台用户"


class User(AbstractUser):
    username = models.CharField(
        max_length=30, default="", blank=True, verbose_name="用户名"
    )

    mobile = models.CharField(
        max_length=11, unique=True, null=True, blank=True, verbose_name="手机号"
    )
    email = models.EmailField(unique=True, verbose_name="邮箱")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    nickname = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="昵称"
    )
    avator = models.ImageField(
        upload_to="avatar", null=True, blank=True, verbose_name="头像"
    )
    user_type = models.CharField(
        max_length=10, choices=UserType, default="client", verbose_name="用户类型"
    )
    score = models.DecimalField(
        max_digits=10, default=0, decimal_places=2, verbose_name="积分"
    )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    objects = MsUserManager()

    @property
    def is_client(self):
        return self.user_type == UserType.CLIENT

    @property
    def is_manager(self):
        return self.user_type == UserType.MANAGER and self.is_staff

    class Meta:
        db_table = "ms_users"
        verbose_name = "用户"
        verbose_name_plural = verbose_name


class ClientUser(User):
    class Meta:
        proxy = True
        verbose_name = "普通用户"
        verbose_name_plural = verbose_name


class ManagerUser(User):
    class Meta:
        proxy = True
        verbose_name = "后台用户"
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = UserType.MANAGER
            self.is_staff = True
        super().save(*args, **kwargs)


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
