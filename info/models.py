from django.db import models
from django.contrib.auth.models import User

class Info(models.Model): #쉼터 info 모델
    restin = "실내 쉼터"
    restout = "실외 쉼터"
    rest_in_choice = ((restin, "실내 쉼터"), (restout, "실외 쉼터"))

    restinfo = models.CharField(max_length=200) #쉼터이름
    content = models.TextField() #내용
    date = models.DateTimeField() #작성일시
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_info') #사용자
    voter = models.ManyToManyField(User, related_name='voter_info', blank=True) #추천수
    restplace = models.CharField(max_length=20, choices=rest_in_choice, default=restin) #실내/실외 여부
    restpeople = models.CharField(max_length=200, null=True) #수용 가능 인원
    restother = models.CharField(max_length=200, null=True) #편의 시설 및 응급물품 구비

    def __str__(self): #id 값 대신 restinfo 출력
        return self.restinfo

class Photo(models.Model):
    info = models.ForeignKey(Info, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)