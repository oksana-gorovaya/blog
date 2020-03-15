from blog.views import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('signup/', views.signup, name="signup"),
    path('new_post', views.create_post, name='create_post'),
    path('comment/<slug:slug>/', views.add_comment, name='add_comment'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("posts/<slug:slug>/", views.show_post_detail, name="show_post_detail"),
    path("posts/<slug:slug>/accounts/", include('django.contrib.auth.urls')),
    path("posts/<slug:slug>/accounts/logout/accounts/", include('django.contrib.auth.urls')),
]
