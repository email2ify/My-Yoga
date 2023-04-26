def about(request):
    posts = Post.objects.all()
    form = YogaEmailForm()

    return render(request, 'blog/about.html', {'posts': posts, 'form': form})