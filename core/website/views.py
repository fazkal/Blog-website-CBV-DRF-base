from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from .forms import ContactForm,NewsletterForm
# Create your views here.

class IndexView (TemplateView):
    template_name = "website/index.html"

class AboutView(TemplateView):
    template_name = "website/about.html"

class ContactView(FormView):
    template_name = "website/contact.html"
    form_class = ContactForm
    success_url = "/contact"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class NewsletterView(FormView):
    template_name = "website/base.html"
    form_class = NewsletterForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)