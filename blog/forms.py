from django import forms
from blog.models import Comment, Posts


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'email', 'text',)
