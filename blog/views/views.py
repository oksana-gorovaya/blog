
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from blog.models.CommentRepository import CommentRepository
from blog.models.Paginator import Paginator
from blog.models.forms.Story import StoryForm
from blog.models.models import Post
from blog.models.forms.CommentModel import CommentModel
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


def signup_view(request):
    signup_form = UserCreationForm(request.POST)

    if not signup_form.is_valid():
        return render(request, 'signup.html', {'signup_form': signup_form})

    signup_form.save()
    username = signup_form.cleaned_data.get('username')
    password = signup_form.cleaned_data.get('password1')
    user = authenticate(username=username, password=password)
    login(request, user)
    return redirect('home')


def show_story_form(request):
    story_form = StoryForm(data=request.POST)

    if story_form.is_valid():
        new_story = story_form.save(commit=False)
        new_story.author = User.objects.filter(username=request.user).first()
        new_story.save()
        return redirect('home')
    return render(request, 'story.html', {'story_form': story_form})


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)

    comments = post.comments.filter()
    paginator = Paginator(comments, 2)

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, template_name, {
        'post': post,
        'comments': comments,
        'paginator': paginator,
        'page_obj': page_obj,
    })


def add_comment(request, slug):
    parent_id = request.GET.get('comment_id')
    comment_repository = CommentRepository(slug)
    comment_model = CommentModel(data={'email':request.POST.get('email'), 'body':request.POST.get('body'), 'parent_id':request.POST.get('parent_id')})
    if comment_model.is_valid():
        comment_repository.save(comment_model, parent_id)
        return redirect('home')
    return render(request, 'comment_form.html', {'comment_form': comment_model})

