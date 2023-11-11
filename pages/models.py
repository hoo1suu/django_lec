from django.db import models


class CompanyInfo(models.Model):
    objects = None
    title = models.CharField(max_length=200, default='Default Title')
    content = models.TextField()
    image = models.ImageField(upload_to='company_info/')

    def __str__(self):
        return self.title


class MainPage(models.Model):
    title = models.CharField(max_length=200, default='Default Title')
    image = models.ImageField(upload_to='images/')
    text = models.TextField()

    def __str__(self):
        return self.title
# Create your models here.
