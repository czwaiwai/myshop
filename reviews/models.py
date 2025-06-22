from django.db import models


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name="用户"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, verbose_name="商品"
    )
    rating = models.IntegerField(
        choices=[(i, i) for i in range(1, 6)], verbose_name="评分"
    )
    comment = models.TextField(verbose_name="评论")
    images = models.ImageField(
        upload_to="reviews/", null=True, blank=True, verbose_name="图片"
    )
    is_approved = models.BooleanField(default=False, verbose_name="是否审核")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class ReviewReply(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name="评论")
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name="用户"
    )
    content = models.TextField(verbose_name="回复内容")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return f"{self.user.username} - {self.review.id}"
