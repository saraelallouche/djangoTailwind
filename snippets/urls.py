from django.urls import path
from .views import (
    HomePageView,
    HeroSectionsPageView,
    FormLayoutsPageView,
    ContentSectionsPageView,
    FeaturesSectionsPageView,
    CustomUserAddView,
    CustomUserListView,
    CustomUserUpdateView,
    CustomUserDeleteView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("hero_sections", HeroSectionsPageView.as_view(), name="hero_sections"),
    path("form_layouts", FormLayoutsPageView.as_view(), name="form_layout"),
    path("content", ContentSectionsPageView.as_view(), name="content"),
    path("features", FeaturesSectionsPageView.as_view(), name="features"),
    path("user/add", CustomUserAddView.as_view(), name="add_user"),
    path("user/list", CustomUserListView.as_view(), name="user_list"),
    path("userdetail/<int:pk>", CustomUserListView.as_view(), name="user_detail"),
    path("user/<int:pk>/edit", CustomUserUpdateView.as_view(), name="edit_user"),
    path("user/<int:pk>/delete", CustomUserDeleteView.as_view(), name="delete_user"),
]
