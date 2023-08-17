from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import surveyForm

def index(request):
    return render(request,"check/check_index.html")

def create(request):
    if request.method =='POST':
        form = surveyForm(request.POST)
        if form.is_valid():#폼이 유효한가?
            question = form.save(commit=False)#임시 저장해서 객체로 리턴받기
            question.create_date = timezone.now() # 작성일시
            question.save()#저장하기
            return redirect('check:index')
    else:
        form = surveyForm()
    return render(request, 'check/check_form.html', {'form' : form})