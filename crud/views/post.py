from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from ..forms import PostForm
from ..models import Post
from django.db.models import Q

# from ..filters import BlogFilter
from django.shortcuts import render


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class SearchResultsListView(ListView):  # new
    model = Post
    context_object_name = "post_list"
    template_name = "home.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        return Post.objects.filter(
            Q(title__icontains=query) | Q(author__username__icontains=query)
        )


class BlogUpdateView(UpdateView):  # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
