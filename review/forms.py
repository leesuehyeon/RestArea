from django import forms
from review.models import Review, Photo

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['restreview', 'content', 'score']
        widgets = {
            'restreview': forms.Select(attrs={'class': 'form-control', 'rows': 10}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
            'score': forms.Select(attrs={'class': 'form-control', 'rows': 10}),
        }