from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('blogs/', views.BlogListView.as_view(), name='blogs'),
    path('<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
]
