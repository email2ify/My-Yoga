def contact(request):
    posts = Post.objects.all()
    form = YogaEmailForm()

    return render(request, 'blog/contact.html', {'posts': posts, 'form': form})