from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class MainContent(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content_detail', args=[self.id])


class CompanyInfo(models.Model):
    # 필드 정의
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='company_info/')


class MainPages(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='mainpage_images/')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)
