from django.db import models

# Create your models here.


class Post(models.Model):
    """ model for post """

    title = models.CharField(max_length=100)
    description = models.TextField()

    likes = models.IntegerField(default=0)
    comments = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return self.title
