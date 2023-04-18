from django import forms
from .models import Comment, yoga_email

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', 'author']


class yoga_emailForm(forms.ModelForm):
    class Meta:
        model = yoga_email
        fields = ['user', 'email']