from django.db import models
from apps.devtools.models import DevTool

class Idea(models.Model):
    title = models.CharField('제목', max_length=24)
    photo = models.ImageField('이미지', blank=True, upload_to='ideas/%Y%m%d')
    content = models.CharField('내용', max_length=24)
    interest = models.IntegerField('관심도')
    devtool = models.ForeignKey(DevTool, on_delete=models.CASCADE, verbose_name='개발툴')
    is_starred = models.BooleanField("찜하기", default = False)