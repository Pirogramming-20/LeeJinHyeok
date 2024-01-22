from django.db import models

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length = 25)
    content = models.CharField (max_length = 50)
    like = models.IntegerField(default = 0)
    isLiked = models.BooleanField (default = False)
    
class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
