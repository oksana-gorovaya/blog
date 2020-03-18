from blog.models.models import Post


class PostRepository:
    def __init__(self, request):
        self.title = request.POST.get('title')
        self.slug = request.POST.get('slug')
        self.content = request.POST.get('content')
        self.author = request.user

    def save(self):
        return Post.objects.create(
            title=self.title,
            slug=self.slug,
            content=self.content,
            author=self.author
        )
