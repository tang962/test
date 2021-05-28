from django.conf.urls import url
from blog import views

#在应用的urls文件中进行url配置时：
#1.严格匹配开头和结尾
urlpatterns = [
    #通过url函数设置url路由配置项
    url('^index/$', views.index),#建立/index和视图index之间的关系
    url('^currnet_datetime/$',views.currnet_datetime),
    url('^book/$', views.book_list),
    url('^book/(\d+)/$', views.book_detail),

]