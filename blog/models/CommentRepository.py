from django.shortcuts import get_object_or_404

from blog.models.models import Post, Comment


class CommentRepository:
    def __init__(self, request, slug):
        self.post = self._get_post(slug)
        self.email = request.POST.get('email')
        self.body = request.POST.get('body')
        self.parent_id = request.GET.get('comment_id')

    def _get_post(self, slug):
        return get_object_or_404(Post, slug=slug)

    def save(self):
        Comment.objects.create(
            post=self.post,
            email=self.email,
            body=self.body,
            parent_id=self.parent_id
        )
