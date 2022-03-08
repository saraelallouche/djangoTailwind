from django.shortcuts import render
from django.views.generic import ListView, DetailView
from ..models import Post
from django.db.models import Q

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class SearchResultsListView(ListView):  # new
    model = Post
    context_object_name = "home"
    template_name = "search_results.html"

    def get_queryset(self):  # new
        return Post.objects.filter(
            Q(title__icontains="author") | Q(title__icontains="title")
        )
