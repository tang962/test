from django.conf import settings

from blog.models import BookInfo


def testdb():
    test1 = BookInfo(btitle = '悟空传',bpub_date =2021-5-25)
    test1.save()
