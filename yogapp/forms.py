from django import forms
from .models import Comment, YogaEmail

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']


class YogaEmailForm(forms.ModelForm):
    class Meta:
        model = YogaEmail
        fields = ['email']