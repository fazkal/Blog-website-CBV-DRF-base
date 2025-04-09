from django.views.generic.base import TemplateView

# TemplateView for display posts
class BlogsView(TemplateView):
    template_name = "blog/blog-home.html"


# TemplateView for display a single post
class BlogSingleView(TemplateView):
    template_name = "blog/blog-single.html"
