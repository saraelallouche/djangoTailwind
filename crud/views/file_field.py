from attr import field
from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from ..models.file_field import File
from django.urls import reverse
import logging


class CustomFileAddView(CreateView):
    model = File
    template_name = "file_field/add.html"
    fields = "__all__"
    success_url = reverse_lazy("file_list")

    # def form_invalid(self, form):
    #     logger.info("form_invalid called")
    #     form.instance.user = self.request.user
    #     print(form.errors)
    #     return super(CustomUserAddView, self).form_invalid(form)


# class CustomFileDetailView(DetailView):
#     model = File
#     template_name = "user/user_detail.html"


class CustomFileListView(ListView):
    model = File
    template_name = "file_field/list.html"
