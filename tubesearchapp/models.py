from django.db import models
from django.utils import timezone
import requests
import re
from apiclient import discovery

# Create your models here.

class AmarakuModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(null=True, blank=True)

    # url情報
    kerword = models.CharField(max_length=50)

    #日付 デフォルトで今日の日付
    register_date = models.DateField(null=True, blank=True, default=timezone.now)
    last_date = models.DateField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.title

# youtube検索の関数
def get_search(keyword):
    youtube = discovery.build('youtube', 'v3', developerkey=api_key)
    youtube_query = youtube.search().list(q=keyword, part='id,snippet', maxResults=5)
    youtube_res = youtube_query.execute()
    return youtube_res.get('item', [])