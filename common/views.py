from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) #사용자 인증
            login(request, user) #로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

def error400(request, exception=None):
    return render(request, 'common/400.html', {})
def error403(request, exception=None):
    return render(request, 'common/403.html', {})
def error404(request, exception=None):
    return render(request, 'common/404.html', {})
def error500(request, exception=None):
    return render(request, 'common/500.html', {})