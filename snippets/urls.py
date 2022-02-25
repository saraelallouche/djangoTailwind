from django.urls import path
from . import views
from .views.templateview import (
    HomePageView,
    HeroSectionsPageView,
    FormLayoutsPageView,
    ContentSectionsPageView,
    FeaturesSectionsPageView,
)
from .views.customuser import (
    CustomUserAddView,
    CustomUserListView,
    CustomUserUpdateView,
    CustomUserDeleteView,
    CustomUserDetailView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("hero_sections", HeroSectionsPageView.as_view(), name="hero_sections"),
    path("form_layouts", FormLayoutsPageView.as_view(), name="form_layout"),
    path("content", ContentSectionsPageView.as_view(), name="content"),
    path("features", FeaturesSectionsPageView.as_view(), name="features"),
    # CustomUser
    path("user/add", CustomUserAddView.as_view(), name="user_add"),
    path("user/list", CustomUserListView.as_view(), name="user_list"),
    path("userdetail/<int:pk>", CustomUserDetailView.as_view(), name="user_detail"),
    path("user/<int:pk>/edit", CustomUserUpdateView.as_view(), name="user_edit"),
    path("user/<int:pk>/delete", CustomUserDeleteView.as_view(), name="user_delete"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
