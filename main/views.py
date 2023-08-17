from django.shortcuts import render, get_object_or_404
from info.models import Info
from django.db.models import Count
from django.db.models import Q
from collections import Counter

def index(request): #메인 화면
    info_list = Info.objects.annotate(num_voter=Count('voter')).order_by('-num_voter')
    context = {'info_list': info_list}
    return render(request, 'main/main.html', context)

def detail(request, info_id): #쉼터 info 상세
    info = get_object_or_404(Info, pk=info_id)
    context = {'info': info}
    return render(request, 'info/info_detail.html', context)

kw_list = list() #검색어 리스트
def search(request): #검색 기능 및 실시간 인기 검색어 도출
    info_list = Info.objects.order_by('-date')

    kw = request.GET.get('kw', '') #검색어
    kw_list.append(kw) #검색어 리스트
    max_list = Counter(kw_list).most_common(n=10) #가장 많이 검색된 검색어 5개 찾기

    if kw:
        info_list = info_list.filter(
            Q(restinfo__icontains=kw) | #쉼터 검색
            Q(content__icontains=kw) #내용 검색
        ).distinct()
    context = {'info_list': info_list, 'kw': kw, 'max_list': max_list}
    return render(request, 'main/main_search.html', context)