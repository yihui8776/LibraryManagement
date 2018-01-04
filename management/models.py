from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)
    contact = models.CharField(max_length=20)  #联系方式

    #def __unicode__(self):  #2
    def __str__(self):     #3
        return self.user.username


#class Book(models.Model):
 #   name = models.CharField(max_length=128)
  #  price = models.FloatField()
   # author = models.CharField(max_length=128)
  #  publish_date = models.DateField()
  #  category = models.CharField(max_length=128)
  #  class META:
  #      ordering = ['name']

    #def __unicode__(self):
#    def __str__(self):
 #       return self.name

class Book(models.Model):
    class Meta:
        verbose_name = '图书'
        verbose_name_plural = verbose_name

    isbn = models.CharField('ISBN', max_length=13, unique=True,default="")
    title = models.CharField('书名', max_length=200)
    subtitle = models.CharField('副标题', max_length=200, blank=True, null=True)
    pages = models.IntegerField('页数', blank=True, null=True)
    author = models.CharField('作者', max_length=60)
    translator = models.CharField('译者', max_length=60, blank=True, null=True)
    price = models.CharField('价格', max_length=60, blank=True, null=True)
    publisher = models.CharField('出版社', max_length=200, blank=True, null=True)
    pubdate = models.CharField('出版日期', max_length=60, blank=True, null=True)
    cover_img = models.URLField('封面图', blank=True, null=True)
    summary = models.TextField('内容简介', blank=True, max_length=2000)
    author_intro = models.TextField('作者简介', blank=True, max_length=2000, null=True)
    category = models.CharField('类别',max_length=128, null=True)
    owner = models.ForeignKey(User) 

    def __str__(self):
        return str(self.title)
  

class Img(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    img = models.ImageField(upload_to='image/%Y/%m/%d/')
    book = models.ForeignKey(Book)

    class META:
        ordering = ['name']

    #def __unicode__(self):
    def __str__(self):
        return self.name

