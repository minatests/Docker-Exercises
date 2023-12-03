from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()
    dp = models.ImageField(upload_to= 'media/images', default='media/images/profile-icon-design-free-vector_9vWQwhV.jpg')

    def __str__(self) -> str:
        return self.name  