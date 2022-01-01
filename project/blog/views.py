from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post, Comments
from .forms import PostForm

def post_list(request):
    posts = Post.objects.all()#.filter(id=1)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})
#zapisanie formularza
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def comment_list(request):
    comment = Coments.objects.all()#.filter(id=1)
    return render(request, 'blog/comment_list.html', {'comments': comments})

def comment_detail(request, pk):
    comment = get_object_or_404(Post, pk=pk)
    Coments.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'comment':comment})



# Create your views here.
