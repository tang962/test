from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,RequestContext,Context
from django import template
import datetime

# Create your views here.
#1.定义视图函数，httprequest
#2.进行url配置，建立url地址和视图的对应关系
#http://127.0.0.1:8000/index


def index(request):
    #进行处理，如果和数据库就是和M，如果要生成网页就和T模板
    #
    d = {"name": "老魏",
         "age": 35,
         "hobby": ["看书", "看电影"],
         "friend": {"name": "小张", "age": 26},
         "pet": ("二哈", "黑白色"),
         "list":list(range(1,9))
         }
    return render(request,'blog/index.html',d)

def currnet_datetime(request):
    text = {}
    now=datetime.datetime.now()
    text['now'] = now
    return render(request,'blog/currnet_datetime.html',text)




