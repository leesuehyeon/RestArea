from django.db import models
from info.models import Info
from django.contrib.auth.models import User

class Review(models.Model): #쉼터 review 모델
    one = "평점: (1/5)"
    two = "평점: (2/5)"
    three = "평점: (3/5)"
    four = "평점: (4/5)"
    five = "평점: (5/5)"
    score_in_choice = ((one, "1"), (two, "2"), (three, "3"), (four, "4"), (five, "5"))

    restreview = models.ForeignKey(Info, on_delete=models.PROTECT) #Info 모델과 연결
    content = models.TextField() #내용
    date = models.DateTimeField(null=True, blank=True) #작성일시
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_review') #사용자
    score = models.CharField(max_length=20, choices=score_in_choice, default=five) #평점

class Photo(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=True)
    image = models.ImageField(blank=True, null=True)