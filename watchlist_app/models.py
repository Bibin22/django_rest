from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Movies(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class StreamingPlatform(models.Model):
    name = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)

    def __str__(self):
        return str(self.name)


class WatchList(models.Model):
    title = models.CharField(max_length=100)
    story_line = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamingPlatform, null=True, blank=True, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.watchlist)