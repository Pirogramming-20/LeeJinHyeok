from django.db import models

# Create your models here.
class Review (models.Model):
    title = models.CharField(max_length = 32)
    year = models.IntegerField()
    genre = models.CharField(max_length = 32)
    score = models.FloatField()
    runtime = models.IntegerField()
    content = models.TextField()
    director = models.CharField(max_length = 32)
    actor = models.CharField(max_length = 64)