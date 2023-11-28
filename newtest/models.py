from django.db import models

# Create your models here.
class Test(models.Model):
    mid = models.IntegerField(default=0, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='藥名')
    color = models.CharField(max_length=255, verbose_name='顏色')
    shape = models.CharField(max_length=255, verbose_name='形狀')
    usee = models.CharField(max_length=255, verbose_name='劑型')
    effect =models.CharField(max_length=255, verbose_name='作用')
    sideffect=models.CharField(max_length=255, verbose_name='副作用')
    img=models.CharField(max_length=255, verbose_name='圖片網址')
    type=models.CharField(max_length=255, verbose_name='藥物類型')

    def __str__(self):
        return 'name{}'.format(self.name)
    
    class Meta:
        verbose_name = '藥物資料庫'
        verbose_name_plural = verbose_name



