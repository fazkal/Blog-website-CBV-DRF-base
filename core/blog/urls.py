from django.urls import path, include
from . import views

app_name = "blog"

urlpatterns = [

    path("api/v1/", include("blog.api.v1.urls")),
    path("",views.BlogsView.as_view(),name="index"),
    path("<int:pk>/",views.BlogSingleView.as_view(),name="single"),
    path("create/",views.PostCreateView.as_view(),name="create"),
    path("post-form/", views.PostFormView.as_view(), name="post_form")
]