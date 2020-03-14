from django.shortcuts import get_object_or_404

from blog.models.Reply import Reply
from blog.models.models import Post, Comment


class CommentRepository:
    def __init__(self, slug):
        self.post = self._get_post(slug)

    def _get_post(self, slug):
        return get_object_or_404(Post, slug=slug)

    def save(self, comment_form, parent_id):
        new_comment = comment_form.save(commit=False)
        new_comment.post = self.post
        new_comment.parent_id = parent_id
        Comment.objects.rebuild()
        new_comment.save()


