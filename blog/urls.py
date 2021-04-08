from django.urls import path
from .views import AuthorDetailView

urlpatterns = [
    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-detail')
]
