# blog/urls.py
from django.urls import path
from ..views import (
    BlogListView,
    BlogDetailView,
    SearchResultsListView,
    BlogDeleteView,
    BlogUpdateView,
)

urlpatterns = [
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
