from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from ..models.customuser import CustomUser
import logging


logger = logging.getLogger(__name__)


class CustomUserAddView(CreateView):
    model = CustomUser
    template_name = "user/add_user.html"
    fields = "__all__"

    def form_invalid(self, form):
        logger.info("form_invalid called")
        form.instance.user = self.request.user
        print(form.errors)
        return super(CustomUserAddView, self).form_invalid(form)


class CustomUserDetailView(DetailView):
    model = CustomUser
    template_name = "user/user_detail.html"


class CustomUserListView(ListView):
    model = CustomUser
    template_name = "user/user_list.html"
    context_object_name = "user_list"
    success_url = reverse_lazy("user_list")


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    template_name = "user/edit_user.html"
    context_object_name = "user_edit"
    fields = "__all__"


def form_invalid(self, form):
    logger.info("form_invalid called")
    form.instance.user = self.request.user
    print(form.errors)
    return super(CustomUserAddView, self).form_invalid(form)


class CustomUserDeleteView(DeleteView):
    model = CustomUser
    template_name = "user/delete_user.html"
    success_url = reverse_lazy("user_list")
