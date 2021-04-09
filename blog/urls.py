from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('create',
         views.AddBlogView.as_view(), name='add-blog'),
    path('<int:blog_id>/comment/create',
         views.AddCommentView.as_view(), name='add-comment'),
    path('<int:blog_id>/comment/<int:pk>/edit',
         views.EditCommentView.as_view(), name='edit-comment'),
    path('<int:blog_id>/comment/<int:pk>/detele',
         views.DeleteCommentView.as_view(), name='delete-comment'),
]
