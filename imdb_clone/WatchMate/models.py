from django.db import models


# Create your models here.
class StreamPlateform(models.Model):
    title = models.CharField(max_length=50)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    active = models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform=models.ForeignKey(StreamPlateform,on_delete=models.CASCADE,related_name="watchlist")
    active = models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title