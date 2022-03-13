from django.urls.base import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)

# from ..forms import PostForm
from ..models import Post
from django.db.models import Q

# from ..filters import BlogFilter
from django.shortcuts import render


# Create your views here.
class BlogListView(ListView):
    paginate_by = 15
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class SearchResultsListView(ListView):  # new
    model = Post
    context_object_name = "post_list"
    template_name = "home.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        return context

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        query_words = query.split(" ")
        # https://stackoverflow.com/questions/46695150/django-search-fields-in-multiple-models
        # https://www.codingforentrepreneurs.com/blog/a-multiple-model-django-search-engine/
        search_fields = ["title", "body"]  #  fields of the same Model
        print(query_words)

        and_lookup = Q()
        for query_word in query_words:
            search_queries = [
                Q(**{field + "__icontains": query_word}) for field in search_fields
            ]
            or_lookup = Q()
            for query in search_queries:
                or_lookup = or_lookup | query
            and_lookup = and_lookup & or_lookup

        qs = sorted(
            Post.objects.filter(and_lookup).distinct(),
            key=lambda instance: instance.pk,
            reverse=True,
        )
        return qs


class BlogCreateView(CreateView):  # new
    model = Post
    template_name = "post_create.html"
    fields = "__all__"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BlogCreateView, self).form_valid(form)

    def form_invalid(self, form):
        form.instance.user = self.request.user
        print(form.errors)
        return super(BlogCreateView, self).form_invalid(form)


class BlogUpdateView(UpdateView):  # new
    model = Post
    template_name = "post_edit.html"
    fields = "__all__"
    success_url = reverse_lazy("home")


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
