from django.db import models
from django.utils import timezone
import os


class Post(models.Model):

    def get_image_path(instance, filename):
        return os.path.join('photos', str(instance.id), filename)

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):

    author = models.ForeignKey('auth.User')
    text = models.TextField()
    created_date = models.DateTimeField(
                default=timezone.now)
    post = models.ForeignKey('Post', related_name='comment')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text
