from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from ..models.customuser import CustomUserModel
from django.urls import reverse
from ..forms import CustomUser
import logging


logger = logging.getLogger(__name__)


class CustomUserAddView(CreateView):
    model = CustomUserModel
    template_name = "user/add_user.html"
    form_class = CustomUser
    success_url = reverse_lazy("user_list")

    # def form_invalid(self, form):
    #     logger.info("form_invalid called")
    #     form.instance.user = self.request.user
    #     print(form.errors)
    #     return super(CustomUserAddView, self).form_invalid(form)


class CustomUserDetailView(DetailView):
    model = CustomUserModel
    template_name = "user/user_detail.html"


class CustomUserListView(ListView):
    model = CustomUserModel
    template_name = "user/user_list.html"


class CustomUserUpdateView(UpdateView):
    model = CustomUserModel
    template_name = "user/edit_user.html"
    form_class = CustomUser
    success_url = reverse_lazy("user_list")


def get_success_url(self):
    return reverse("user_list", kwargs={"pk": self.kwargs["pk"]})


class CustomUserDeleteView(DeleteView):
    model = CustomUserModel
    template_name = "user/delete_user.html"
    success_url = reverse_lazy("user_list")
