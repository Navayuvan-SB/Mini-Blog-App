from django.urls import path
from .views import AuthorDetailView, BlogDetailView

urlpatterns = [
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
]
