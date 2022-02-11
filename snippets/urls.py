from django.urls import path
from .views import HomePageView, HeroSectionsPageView, FormLayoutsPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("hero_sections", HeroSectionsPageView.as_view(), name="hero_sections"),
    path("form_layouts", FormLayoutsPageView.as_view(), name="form_layout"),

]