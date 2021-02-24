from django.db import models
from django.utils import timezone
import requests
import re
from bs4 import BeautifulSoup

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

    def __str__(self):
        return self.title

def get_price_ama(page_url):
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, features="lxml")
    selected_html = soup.select('.a-span12 span.a-color-price')

    if not selected_html:
        selected_html = soup.select('.a-color-base span.a-color-price')

    pattern = r'\d*,?\d*,?\d*\d'
    regex = re.compile(pattern)
    matches = re.findall(regex, selected_html[0].text)
    price = matches[0].replace(',', '')
    price = 0
    return int(price)

def get_price_raku(page_url):
    price = 0
    return int(price)
