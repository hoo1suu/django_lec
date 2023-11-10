from django.db import models
from django.urls import reverse


class MainContent(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('content_detail', args=[self.id])
