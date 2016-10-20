from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
from django.utils import timezone


# Create your models here.
class Categories(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_blog_category', None, {'slug': self.slug}


class Posts(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Post Title')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='URL')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    meta_description = models.CharField(max_length=500, verbose_name='Meta Description', blank=True)
    meta_keywords = models.CharField(max_length=250, verbose_name='Meta Keywords', blank=True)
    body = models.TextField()
    category = models.ForeignKey(Categories)
    published = models.BooleanField(default=None)
    author = models.ForeignKey(User, null=True, blank=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Posts"

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_blog_post', None, {'slug': self.slug}


class Comment(models.Model):
    post = models.ForeignKey('blog.Posts', related_name='comments')
    author = models.CharField(max_length=200)
    email = models.EmailField(max_length=75)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
