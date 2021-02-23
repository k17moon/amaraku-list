from django.db import models
from django.utils import timezone


# Create your models here.

class AmarakuModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(null=True, blank=True)
    # url情報
    url_ama = models.URLField(max_length=1000, null=True, blank=True, default='')
    url_raku = models.URLField(max_length=1000, null=True, blank=True, default='')

    # 価格情報
    price_ama = models.IntegerField(null=True, blank=True)
    price_raku = models.IntegerField(null=True, blank=True)
    lowest_ama = models.IntegerField(null=True, blank=True)
    lowest_raku = models.IntegerField(null=True, blank=True)

    #日付 デフォルトで今日の日付
    register_date = models.DateField(null=True, blank=True, default=timezone.now)
    last_date = models.DateField(null=True, blank=True, default=timezone.now)
