from django.db import models

# Create your models here.

class Topic(models.Model):
    # 用户学习的主题
    # 字段含义 https://docs.djangoproject.com/en/1.8/ref/models/fields/#blank
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        #返回模型的字符串表示
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'
    def __str__(self):
        return self.text[:50]+'....'