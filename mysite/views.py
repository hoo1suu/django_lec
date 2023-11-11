from django.shortcuts import render, get_object_or_404
from . import models


def index(request):
    content_list = models.MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'mysite/content_list.html', context)


def content_detail(request, id):
    content = get_object_or_404(models.MainContent, pk=id)
    return render(request, 'content_detail.html', {'content': content})
