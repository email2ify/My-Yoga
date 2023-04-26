def frontpage(request):
    posts = Post.objects.all()
    form = YogaEmailForm()

    return render(request, 'blog/frontpage.html', {'posts': posts, 'form': form})