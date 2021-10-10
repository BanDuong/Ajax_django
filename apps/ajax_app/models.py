from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="create")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="update")

    class Meta:
        abstract = True


class Product(TimeStamp):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="product")
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="name")
    quantity = models.IntegerField(null=True, blank=True, verbose_name="quantity")
    image = models.ImageField(null=True, blank=True, verbose_name="image", upload_to="static/images/")
    description = models.TextField(null=True, blank=True, verbose_name="description")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tbl_product"
        verbose_name_plural = "product"
