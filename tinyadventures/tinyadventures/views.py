"""Base views for Tiny Adventures."""
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(TemplateView):
    """Home view for Tiny Adventures."""
    template_name = 'tinyadventures/home.html'
