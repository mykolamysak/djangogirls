from django.contrib import admin
from .models import Post, Comment
from .forms import PostForm, CommentForm

admin.site.register(Post)
admin.site.register(Comment)
