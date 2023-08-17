from django.shortcuts import render, get_object_or_404, redirect
from .models import Info
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Count

def index(request): #쉼터 info 목록
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '') #검색어
    so = request.GET.get('sortKind', '최신순') #정렬 방식
    info_list = Info.objects.order_by('-date')

    if so == "최신순":
        info_list = Info.objects.order_by('-date')
    elif so == "추천순":
        info_list = Info.objects.annotate(num_voter=Count('voter')).order_by('-num_voter')

    if kw:
        info_list = info_list.filter(
            Q(restinfo__icontains=kw) | #쉼터 검색
            Q(content__icontains=kw) #내용 검색
        ).distinct()
    paginator = Paginator(info_list, 10)  #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'info_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'info/info_index.html', context)

def detail(request, info_id): #쉼터 info 상세
    info = get_object_or_404(Info, pk=info_id)
    context = {'info': info}
    return render(request, 'info/info_detail.html', context)

@login_required(login_url='common:login')
def vote(request, info_id): #쉼터 info 추천
    info = get_object_or_404(Info, pk=info_id)
    info.voter.add(request.user)
    return redirect('info:detail', info_id=info.id)