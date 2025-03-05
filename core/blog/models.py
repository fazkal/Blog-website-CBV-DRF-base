from django.db import models


# Create your models here.

class Post(models.Model):
    """this is a class to define post for blog app"""

    author = models.ForeignKey("accounts.profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("category", on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:20]


class Category(models.Model):
    """this is a class to define category for blog app"""
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name