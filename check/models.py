from django.db import models

class Survey(models.Model):
    one = "포털사이트"#db에 저장되는 이름
    two = "지인 추천"
    three = "Sns"
    four = "주소직접 입력"
    five = "기타"

    choices = ((one,"포털사이트"),(two,"지인 추천"),(three,"Sns"),(four,"주소직접 입력"),(five,"기타"))

    Sone = "매우만족"
    Stwo = "만족"
    Sthree = "보통"
    Sfour = "불만족"
    Sfive = "매우 불만족"

    satisfaction = ((Sone , "매우만족"),(Stwo , "만족"),(Sthree , "보통"),(Sfour , "불만족"),(Sfive , "매우 불만족"))

    score_1 = models.TextField(max_length=20, choices=choices, default=one)
    score_2 = models.TextField(max_length=20, choices=satisfaction, default=Sone)
    content_1 = models.TextField()  # 내용
    content_2 = models.TextField()  # 내용
    date = models.DateTimeField(null=True, blank=True)  # 작성 일시