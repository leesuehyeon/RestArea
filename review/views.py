import os.path

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Review, Photo
from .forms import ReviewForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q

#로깅 설정
# import logging
# logger = logging.getLogger('RestArea')

#업로드 하는 파일 개수, 크기, 확장자 제한
FILE_COUNT_LIMIT = 4 #4개
FILE_SIZE_LIMIT = 4194304 #4MB
WHITE_LIST_EXT = {
    '.JPG',
    '.jpg',
    '.JPEG'
    '.jpeg',
} #이미지 확장자

def index(request): #쉼터 review 목록
    #logger.info("INFO 레벨로 출력") #로깅
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '') #검색어
    review_list = Review.objects.order_by('-date')
    if kw:
        review_list = review_list.filter(
            Q(restreview__restinfo__icontains=kw) |
            Q(content__icontains=kw) | #내용 검색
            Q(author__username__icontains=kw) #글쓴이 검색
        ).distinct()
    paginator = Paginator(review_list, 10) #페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'review_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'review/review_index.html', context)

@login_required(login_url='common:login')
def create(request): #쉼터 review 작성
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user #author 속성에 로그인 계정 저장
            review.date = timezone.now()
            review.save()

            for img in request.FILES.getlist('imgs'):
                #파일 개수 제한
                if len(request.FILES.getlist('imgs')) > FILE_COUNT_LIMIT:
                    review.delete()
                    return render(request, 'review/review_error_1.html')

                #파일 크기 제한
                if img.size > FILE_SIZE_LIMIT:
                    review.delete()
                    return render(request, 'review/review_error_2.html')

                #파일 확장자 체크
                img_name, img_ext = os.path.splitext(img.name)
                if img_ext not in WHITE_LIST_EXT:
                    review.delete()
                    return render(request, 'review/review_error_3.html')

                photo = Photo()
                photo.review = review
                photo.image = img
                photo.save()
            return redirect('review:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'review/review_create.html', context)

@login_required(login_url='common:login')
def modify(request, review_id): #쉼터 review 수정
    review = get_object_or_404(Review, pk=review_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user #author 속성에 로그인 계정 저장
            review.date = timezone.now()
            review.save()
            for img in request.FILES.getlist('imgs'):
                # 파일 개수 제한
                if len(request.FILES.getlist('imgs')) > FILE_COUNT_LIMIT:
                    return render(request, 'review/review_error_1.html')

                # 파일 크기 제한
                if img.size > FILE_SIZE_LIMIT:
                    return render(request, 'review/review_error_2.html')

                # 파일 확장자 체크
                img_name, img_ext = os.path.splitext(img.name)
                if img_ext not in WHITE_LIST_EXT:
                    return render(request, 'review/review_error_3.html')

                photo = Photo()
                photo.review = review
                photo.image = img
                photo.save()
            return redirect('review:index')
    else:
        form = ReviewForm()
    context = {'form': form}
    return render(request, 'review/review_create.html', context)

@login_required(login_url='common:login')
def delete(request, review_id): #쉼터 review 삭제
    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    return redirect('review:index')