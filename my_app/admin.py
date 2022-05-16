from django.contrib import admin

# Register your models here.
from my_app.models import Project


# 优化列表
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_name", "project_type","project_version")


admin.site.register(Project, ProjectAdmin)

# 全局更改
admin.site.site_header = '平台管理666'
admin.site.site_title = '轮哥标题'
