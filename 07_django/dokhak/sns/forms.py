from django import forms
from .models import Comment, Posting


class PostingModelForm(forms.ModelForm):
    class Meta:
        model = Posting
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
