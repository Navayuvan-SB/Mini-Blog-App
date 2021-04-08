from django.contrib import admin
from .models import Author, Blog, Content, Comment


class ContentInline(admin.TabularInline):
    model = Content
    extra = 2


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blogger', 'post_date')
    inlines = [ContentInline, CommentInline]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')
