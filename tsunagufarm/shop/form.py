
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    text = forms.CharField(label="応援コメント", widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['text']
