from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import Post

# TemplateView for display posts
class BlogsView(ListView):
    model = Post
    paginate_by = 2
    template_name = "blog/blog-home.html"


# TemplateView for display a single post
class BlogSingleView(TemplateView):
    template_name = "blog/blog-single.html"
