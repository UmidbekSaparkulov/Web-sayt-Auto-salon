from django.contrib import admin
from .models import Blog, Tag, Comment, Category, Subscribe
admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Subscribe)