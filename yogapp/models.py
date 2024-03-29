from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]


class YogaEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='Emailaddress')
    email = models.EmailField()

    def __str__(self):
        return self.email
