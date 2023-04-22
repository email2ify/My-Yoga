from django.contrib import admin
from .models import Post, YogaEmail, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)

admin.site.register(YogaEmail)
