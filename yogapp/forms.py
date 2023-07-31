from django import forms
from .models import Comment, YogaEmail


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class YogaEmailForm(forms.ModelForm):
    class Meta:
        model = YogaEmail
        fields = ['email']
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
