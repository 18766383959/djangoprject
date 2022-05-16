from django.db import models

# Create your models here.
from django.db import models
PROJECT_TYPE = [(0,'APP'),
                (1,'WEB'),
                (2,'其他')]
# Create your models here.
#主要是数据库的操作
class Project(models.Model):
    #字段的名称
    #项目经名称
    project_name = models.CharField(max_length=200,blank=False,verbose_name="项目名称")
    #项目类型
    project_type = models.SmallIntegerField(blank=False,choices=PROJECT_TYPE,verbose_name="项目类型")
    #项目版本
    project_version = models.CharField(max_length=200,blank=False,verbose_name="项目版本")

    class Meta:
        verbose_name = '测试项目管理'
        verbose_name_plural = verbose_name
