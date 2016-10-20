from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^view/(?P<slug>[^\.]+)', views.view_blog_post, name='view_blog_post'),
    url(r'^category/(?P<slug>[^\.]+)', views.view_blog_category, name='view_blog_category'),
    url(r'^post/(?P<slug>[^\.]+)', views.add_comment_to_post, name='add_comment_to_post'),
]
