from blog.models.models import Comment
from django import forms


class CommentModel(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('email', 'body')
