from django.db import models
from mymap.utils import thumbnail
from django.db.models.signals import pre_save
from django.core.files import File

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, null=True)
    lnglat = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[1].strip()
        return None

    @property
    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0].strip()
        return None


class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)


def pre_on_post_save(sender, **kwargs):
    post = kwargs['instance']
    if post.photo:
        max_width = 300
        if post.photo.width > max_width or post.photo.height > max_width:
            processed_file = thumbnail(post.photo.file, max_width, max_width)
            # processed_file = square_image(post.image.file, max_width)
            post.photo.save(post.photo.name, File(processed_file))

pre_save.connect(pre_on_post_save, sender=Post)
