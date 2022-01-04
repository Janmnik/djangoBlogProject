from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .models import Post, Comments
from .forms import PostForm, CommentForm

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

#lista ktywnych komentarzy dla danego posta
#comments = post.comments.filter(active=True)

#def comment_detail(request):
#if request.method == 'POST':
    #komentarz zostanie upublikowany
 #   comment_form = CommentForm(data=request.POST)
  #  if comment_form.is_valid():
        #Utworzenie obiektu comment
   #     new_comment = comment_form.save(commit=False)
        #Przypisanie komentarza do danego posta
    #    new_comment.post = post
        #zapisanie komentarza w abzie danych
     #   new_comment.save()
   #else:
    #    comment_form = CommentForm()
#return render(request, 'blog/post_detail.html', {'comments': comments, 'comments_form': comments_form})


#def comment_list(request):
 #   comment = Coments.objects.filter(active = True)#all()#.filter(id=1)
  #  return render(request, 'blog/comment_list.html', {'comments': comments})

#def comment_detail(request, pk):
 #   comment = get_object_or_404(Commments, pk=pk)
  #  Comments.objects.get(pk=pk)
   # return render(request, 'blog/post_detail.html', {'comment':comment})


def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})



# Create your views here.
