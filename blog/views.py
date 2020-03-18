from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from blog.models.CommentRepository import CommentRepository
from blog.models.PostRepository import PostRepository
from blog.models.Pagination import Pagination
from blog.models.forms.PostModel import PostModel
from blog.models.models import Post
from blog.models.forms.CommentModel import CommentModel
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'


def signup(request):
    signup_form = UserCreationForm(request.POST)

    if not signup_form.is_valid():
        return render(request, 'signup.html', {'signup_form': signup_form})

    signup_form.save()
    username = signup_form.cleaned_data.get('username')
    password = signup_form.cleaned_data.get('password1')
    user = authenticate(username=username, password=password)
    login(request, user)
    return redirect('home')


def create_post(request):
    post_form = PostModel(data=request.POST)
    if not post_form.is_valid():
        return render(request, 'post.html', {'post_form': post_form})

    PostRepository(request).save()

    return redirect('home')


def show_post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)

    comments = post.comments.filter()
    pagination = Pagination(comments, 2)

    page_number = request.GET.get('page', 1)
    page_content = pagination.generate_content(page_number)
    page = pagination.get_page(page_number)

    return render(request, template_name, {
        'post': post,
        'comments': comments,
        'pagination': pagination,
        'page_content': page_content,
        'page': page
    })


def add_comment(request, slug):
    comment_model = CommentModel(data=request.POST)
    if not comment_model.is_valid():
        return render(request, 'comment_form.html', {'comment_form': comment_model})

    CommentRepository(request, slug).save()

    return redirect('home')

