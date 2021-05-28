from django.contrib import admin
from blog.models import BookInfo,HeroInfo
#后台管理相关文件
# Register your models here.
class BookInfoAdmin(admin.ModelAdmin):
    #图书模型管理类
    list_display = ['id','btitle','bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgender','hcomment','hbook']
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
