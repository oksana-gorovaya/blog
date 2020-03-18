from blog.views import PostList, signup, create_post, add_comment, show_post_detail
from django.urls import path, include

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('signup/', signup, name="signup"),
    path('new_post', create_post, name='create_post'),
    path('comment/<slug:slug>/', add_comment, name='add_comment'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("posts/<slug:slug>/", show_post_detail, name="show_post_detail"),
    path("posts/<slug:slug>/accounts/", include('django.contrib.auth.urls')),
    path("posts/<slug:slug>/accounts/logout/accounts/", include('django.contrib.auth.urls')),
]
