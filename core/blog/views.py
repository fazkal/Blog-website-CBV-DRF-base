from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView,CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from accounts.models import Profile
from .forms import PostForm

# TemplateView for display posts
class BlogsView(ListView):
    model = Post
    paginate_by = 2
    template_name = "blog/blog-home.html"


# TemplateView for display a single post
class BlogSingleView(LoginRequiredMixin,TemplateView):
    template_name = "blog/blog-single.html"
    login_url = '/accounts/login/'  # Optional: Redirect URL if not logged in



class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    # success_url = "/blog/"
    template_name = 'blog/post_form.html'
    login_url = '/accounts/login/'  # Optional: Redirect URL if not logged in


    def form_valid(self, form):
        user_profile = getattr(self.request.user, 'profile', None)
        if user_profile:
            form.instance.author = user_profile
        else:
            # Handle case when profile is missing, e.g., create one or return error
            # You can raise an exception or return an error message
            form.add_error(None, 'User profile does not exist.')
            return self.form_invalid(form)
        return super().form_valid(form)
    

class PostFormView(LoginRequiredMixin,View):
    login_url = '/accounts/login/'  # Optional: Redirect URL if not logged in
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})