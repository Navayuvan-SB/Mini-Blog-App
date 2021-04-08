from django.urls import path


urlpatterns = [
    path('author/<int:pk>', views.AuthorDetailView.as_view(), 'author-detail')
]
