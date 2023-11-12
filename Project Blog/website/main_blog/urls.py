from django.urls import path
from main_blog import views

urlpatterns=[
    path('CreateBlog/',views.CreateBlog.as_view(), name='CreateBlog'),
    path('blog_list/',views.blog_list, name='blog_list'),
    path('read_blog/<int:id>/',views.read_blog, name='read_blog'),
    path('view_blog_profile<int:id>/',views.view_blog_profile, name='view_blog_profile'),
    path('read_blog_slug/<slug:slug>/',views.read_blog_slug, name='read_blog_slug'),
    
    
]