from django.db import models
from django.utils import timezone

import requests
import re
from apiclient import discovery
from django.conf import settings
# YOUTUBE_DATA_V3_API_KEY = "API_Keyの入力"

# Create your models here.
# youtube検索の関数
def get_search(keyword):
    # keyword = self.keyword
    youtube = discovery.build('youtube', 'v3', developerKey=settings.YOUTUBE_DATA_V3_API_KEY)
    youtube_query = youtube.search().list(q=keyword, part='id,snippet', maxResults=3)
    youtube_res = youtube_query.execute()
    return youtube_res.get('items', [])

class TubesearchModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(null=True, blank=True)

    # url情報
    keyword = models.CharField(max_length=50)



    # 以下のように取り出せる
    items = get_search(keyword)
    for item in items:
       print(item['snippet']['title'])
       print("https://www.youtube.com/watch?v="+item['id']['videoId'])


    #日付 デフォルトで今日の日付
    register_date = models.DateField(null=True, blank=True, default=timezone.now)
    last_date = models.DateField(null=True, blank=True, default=timezone.now)

    def __str__(self):
        return self.title


