from django import forms
from check.models import Survey

class surveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['score_1','score_2','content_1','content_2']
        widgets = {
            'score_1': forms.Select(attrs={'class': 'form-control'}),
            'score_2': forms.Select(attrs={'class': 'form-control'}),
            'content_1': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'content_2': forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
        }
        labels = {
            'score_1': '홈페이지의 방문 경로는 무엇입니까?',
            'score_2': '홈페이지에 대한 만족도를 평가해주세요',
            'content_1': '홈페이지에 표기된 정보가 시설 운영 정보와 다른 것이 있다면 적어주세요',
            'content_2': '홈페이지에 대한 개선점이나 추가했으면 하는 정보가 있다면 적어주세요'
        }