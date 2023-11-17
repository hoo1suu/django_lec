from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()  # GET 요청에 대한 폼 인스턴스 생성
    return render(request, 'accounts/signup.html', {'form': form})
