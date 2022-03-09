from django.views.generic import ListView, DetailView
from ..models import Post
from django.db.models import Q

# from ..filters import BlogFilter
from django.shortcuts import render


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        object_list = self.model.objects.all()
        if query:
            object_list = self.model.objects.filter(
                Q(title__icontains=query)
                | Q(body__icontains=query)
                | Q(created__icontains=query)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


# class SearchResultsListView(ListView):  # new
#     model = Post
#     context_object_name = "post"
#     template_name = "search_results.html"
