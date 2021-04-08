from django.db import models
from django.core.validators import MaxValueValidator


class News(models.Model):
    title = models.CharField(max_length=100, blank=False)
    link = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvotes = models.IntegerField(
        default=0, validators=[MaxValueValidator(99)]
    )
    author_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, null=True, related_name="comments"
    )
    author_name = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.news}, {self.author_name}, {self.creation_date}"
