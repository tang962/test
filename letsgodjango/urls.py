"""letsgodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
#这里最外层的urls文件，但这里是项目的urls文件
urlpatterns = [
    path('admin/', admin.site.urls), #这是一个配置项目
    path(r'', include('blog.urls')),#第一个参数是正则匹配，第二个是去哪里进行查找
    #注意：参数进行匹配前，会把已经匹配成功的字符串，去掉，
]
