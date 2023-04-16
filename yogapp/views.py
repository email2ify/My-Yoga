from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .forms import CommentForm, yoga_emailForm
from .models import Post, Comment, yoga_email


def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})


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


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    comment.delete()
    return redirect('frontpage')


def yoga_email(request):

    yoga = request.yoga

    if request.method == 'POST':
        form = EmailAddressForm(request.POST)
        if form.is_valid():
            email_address = form.save(commit=False)
            email_address.yoga = yoga
            email_address.save()
    else:
        form = EmailAddressForm()

    return render(request, 'blog/yoga_email.html', {'form': form})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')
