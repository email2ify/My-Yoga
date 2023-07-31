from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm, YogaEmailForm
from .models import Comment, Post


def frontpage(request):
    """
    Display the frontpage with all posts and a YogaEmailForm.
    """
    posts = Post.objects.all()
    form = YogaEmailForm()

    return render(
        request,
        'blog/frontpage.html',
        {'posts': posts, 'form': form}
    )


def post_detail(request, slug):
    """
    Display the details of a specific post with an option to add a comment.
    """

    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, 'Comment created successfully')

            return redirect('post_detail', slug=post.slug)
        else:
            messages.error(request, 'Error creating comment')
    else:
        form = CommentForm()

    return render(
        request,
        'blog/post_detail.html',
        {'post': post, 'form': form}
    )


def update_comment(request, pk):
    """
    Update an existing comment for a post and display the form.
    """
    comment = get_object_or_404(Comment, id=pk)
    comment_form = CommentForm(instance=comment)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, 'Comment updated successfully')
            return redirect('frontpage')
        else:
            messages.error(request, 'Error updating comment')

    context = {
        'comment': comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog/update_comment.html', context)


def delete_comment(request, pk):
    """
    Delete a specific comment and display a success message.
    """
    comment = get_object_or_404(Comment, id=pk)
    comment.delete()
    messages.success(request, 'Comment deleted successfully')
    return redirect('frontpage')


@login_required
def yoga_email(request):
    """
    Allow logged-in users to submit their YogaEmailForm.
    """

    posts = Post.objects.all()

    if request.method == 'POST':
        form = YogaEmailForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
    else:
        form = YogaEmailForm()

    return render(
        request,
        'blog/frontpage.html',
        {'form': form, 'posts': posts}
    )


def about(request):
    """
    Display the about page.
    """
    return render(request, 'blog/about.html')


def contact(request):
    """
    Display the contact page.
    """
    return render(request, 'blog/contact.html')
