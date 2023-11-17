from django.db import models
from django.urls import reverse


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
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='company_info/')
