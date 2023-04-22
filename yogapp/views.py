from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import CommentForm, YogaEmailForm
from .models import Post, Comment, YogaEmail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin

# userpage


def frontpage(request):
    posts = Post.objects.all()
    form = YogaEmailForm()

    return render(request, 'blog/frontpage.html', {'posts': posts, 'form': form})

# view


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})

# blogs


def post_diet(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_diet', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_diet.html', {'post': post, 'form': form})


def post_balance(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_balance', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_balance.html', {'post': post, 'form': form})


def post_shoulder(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_shoulder', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_shoulder.html', {'post': post, 'form': form})

# update


def update_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    comment_form = CommentForm(instance=comment)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('frontpage')

    context = {
        'comment': comment,
        'comment_form': comment_form,
    }
    return render(request, 'blog/update_comment.html', context)

# delete


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    comment.delete()
    return redirect('frontpage')


@login_required
def yoga_email(request):

    posts = Post.objects.all()

    if request.method == 'POST':
        form = YogaEmailForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
    else:
        form = YogaEmailForm()
    return render(request, 'blog/frontpage.html', {'form': form, 'posts': posts})

# info


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')
