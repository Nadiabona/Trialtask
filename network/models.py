from django.db import models
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from core.models import User

class BaseModel(models.Model):
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now_add=True)

    class Meta:
        abstract = True

def unix():
    return timezone.now().replace(year=1970, month =1, day = 1, hour = 0 , minute=0, second=0, microsecond=0)

class Products(BaseModel):
    product_name = models.CharField(max_length=255,  blank = True, default = "")
    product_model = models.CharField(max_length=255, blank = True, default = "")
    date_to_market = models.DateTimeField(verbose_name="Дата выхода на рынок", default = unix)
    unit = models.ForeignKey("network.Unit", on_delete=models.CASCADE, related_name='products')


    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name

class Unit(BaseModel):
    LEVEL_ZERO = 0
    LEVEL_ONE = 1
    LEVEL_TWO= 2

    LEVEL_CHOICES = (
        (LEVEL_ZERO, "0"),
        (LEVEL_ONE, "1"),
        (LEVEL_TWO, "2"),)

    title = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=False, blank=False)
    country = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    street = models.CharField(max_length=255, null=False, blank=False)
    building_number = models.SmallIntegerField(null=False, blank=False)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=LEVEL_ZERO)
    is_deleted = models.BooleanField(verbose_name="Удален", default=False)
    supplier = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT)
    amount_due_in_kopeeks = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


    def __str__(self):
        return self.title












