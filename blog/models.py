from django.db import models
#设计和表对应的类 模型类
# Create your models here.
class BookInfo(models.Model):
    '''图书模型类'''
    btitle =  models.CharField(max_length=20)
    #btitle是图书名称，CharField说明这是一个字符串，max_length指定字符串的最大长度
    bpub_date = models.DateField()
    # bpub_date是出版日期，DateField说明这是一个日期类型
    def __str__(self):
        #返回书籍名称
        return self.btitle

class HeroInfo(models.Model):
    '''英雄人物关系类'''
    hname = models.CharField(max_length=20)
    #英雄名称
    hgender = models.BooleanField(default=True)
    #性别，默认true，为女
    hcomment = models.CharField(max_length=128)
    hbook = models.ForeignKey('BookInfo',on_delete=models.CASCADE)
    #关系属性 hbook，建立图书类和英雄人物类之间的一对多关系
    #关系属性对应的表的字段名格式：关系属性名_id
    def __str__(self):
        return self.hname
        #返回英雄名
