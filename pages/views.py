from django.shortcuts import render
from .models import CompanyInfo, MainPage


def mainpage(request):
    mainpage_data = MainPage.objects.first()  # 첫 번째 MainPage 인스턴스를 가져옴
    return render(request, 'pages/mainpages.html', {'mainpage': mainpage_data})


def company_info(request):
    info = CompanyInfo.objects.first()  # 첫 번째 CompanyInfo 인스턴스를 가져옴
    return render(request, 'pages/company_info.html', {'company_info': info})


def company(request):
    return render(request, 'content_list.html')
