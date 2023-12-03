from django.db import models
from BlogUsers.models import *
# Create your models here.
# class Author(models.Model):
#     name = models.CharField(max_length=50)
#     bio = models.TextField()

#     def __str__(self) -> str:
#         return self.name   
    

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self) -> str:
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100)  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField()