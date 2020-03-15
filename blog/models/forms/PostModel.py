from django import forms

from blog.models.models import Post


class PostModel(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content')
