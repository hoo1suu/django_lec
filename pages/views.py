from django.shortcuts import render
from .models import CompanyInfo


def mainpage(request):
    return render(request, 'pages/mainpage.html')


def company(request):
    return render(request, 'pages/company_info.html')


def company_info(request):
    info = CompanyInfo.objects.first()  # 첫 번째 CompanyInfo 인스턴스를 가져옴
    return render(request, 'pages/company_info.html', {'company_info': info})
