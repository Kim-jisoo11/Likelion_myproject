from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.title





class Comment(models.Model):
    content = models.CharField(max_length= 100)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)