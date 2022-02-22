from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import CustomUser

import logging


logger = logging.getLogger(__name__)

# from .forms import CustomUserCreateForm
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "home/landing_page.html"


class HeroSectionsPageView(TemplateView):
    template_name = "hero_sections.html"


class FormLayoutsPageView(TemplateView):
    template_name = "form_layout.html"


class ContentSectionsPageView(TemplateView):
    template_name = "content.html"


class FeaturesSectionsPageView(TemplateView):
    template_name = "features.html"


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
    template_name = "user_detail.html"


class CustomUserListView(ListView):
    model = CustomUser
    template_name = "user/user_list.html"
    context_object_name = "user_list"


class CustomUserUpdateView(UpdateView):
    model = CustomUser
    template_name = "user/edit_user.html"
    context_object_name = "edit_user"
    fields = "__all__"


class CustomUserDeleteView(DeleteView):
    model = CustomUser
    template_name = "user/delete_user.html"
    success_url = reverse_lazy("user_list")
