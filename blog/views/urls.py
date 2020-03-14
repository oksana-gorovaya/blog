from blog.views import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('signup/', views.signup_view, name="signup"),
    path('new_story', views.show_story_form, name='show_story_form'),
    path("posts/<slug:slug>/", views.post_detail, name="post_detail"),
    path('comment/<slug:slug>/', views.add_comment, name='add_comment'),
    path('accounts/', include('django.contrib.auth.urls')),
]
