from django.shortcuts import render, get_object_or_404
from blog.models import Posts, Categories
from blog.forms import CommentForm
from django.shortcuts import redirect


# Create your views here.
def blog(request):
    categories = Categories.objects.all()
    posts = Posts.objects.all()[:5]
    context_dict = {'categories': categories, 'posts': posts}
    return render(request, 'blog/blog.html', context=context_dict)


def view_blog_post(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    context_dict = {'post': post}
    return render(request, 'blog/blog_post.html', context=context_dict)


def view_blog_category(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    posts = Posts.objects.filter(category=category)[:5]
    context_dict = {'category': category, 'posts': posts}
    return render(request, 'blog/blog_category.html', context=context_dict)


def add_comment_to_post(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('view_blog_post', slug=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


