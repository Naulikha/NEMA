from django.views.generic import TemplateView
from django.views.generic import CreateView

from .forms import ContactForm, CommentForm


class HomeView(TemplateView):

    template_name = "home.html"


class AboutView(TemplateView):

    template_name = "about.html"


class BlogView(CreateView):

    template_name = "blog.html"
    form_class = CommentForm
    success_url = '/'


class ServicesView(TemplateView):

    template_name = "services.html"


class ContactView(CreateView):

    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/'


