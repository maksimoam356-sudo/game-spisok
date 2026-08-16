from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    release = models.DateField()
    steam_url = models.URLField()
    image_url = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title







