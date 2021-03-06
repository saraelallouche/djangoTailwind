from django.views.generic import TemplateView


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
