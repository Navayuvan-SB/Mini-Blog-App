from django.urls import path
from . import views

urlpatterns = [
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
]
