from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Memoモデルを作成する
class Memo(models.Model):

    # user_memo = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE,default=0 )

    # 日付
    dateData = models.DateField(default=timezone.now, blank=True)

    # 学んだこと
    discovery = models.TextField(blank=True)

    # 学んだこと
    tired = models.TextField(blank=True)

    # 学んだこと
    dislike = models.TextField(blank=True)

    # 学んだこと
    happy = models.TextField(blank=True)

    # 学んだこと
    best = models.TextField(blank=True)

    # 学んだこと
    tomorrow = models.TextField(blank=True)

    # 学んだこと
    other = models.TextField(blank=True)

    # 学んだこと
    summarize = models.TextField(blank=True)

    breakfast = models.ImageField(upload_to='images/breakfast/%Y/%m/%d/%s/', blank=True, null=True)

    # 朝食名
    breakfastName = models.CharField(max_length=30, blank=True)

    lunch = models.ImageField(upload_to='images/lunch/%Y/%m/%d/%s/', blank=True, null=True)

    lunchName = models.CharField(max_length=30, blank=True)

    dinner = models.ImageField(upload_to='images/dinner/%Y/%m/%d/%s/', blank=True, null=True)

    dinnerName = models.CharField(max_length=30, blank=True)

    snack = models.ImageField(upload_to='images/snack/%Y/%m/%d/%s/', blank=True, null=True)

    snackName = models.CharField(max_length=30, blank=True)

    # 食事の総合評価
    mealEvaluation = models.IntegerField(blank=True, default='0')

    # 食事へのコメント
    mealComment = models.TextField(blank=True)

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.discovery


    
