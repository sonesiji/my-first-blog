from django.contrib import admin
from .models import Post, Comment
admin.site.register(Post)
admin.site.register(Comment)
from .models import Feedback

admin.site.register(Feedback)