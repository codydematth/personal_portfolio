from django.utils.text import slugify
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True, upload_to="img", default="placeholder.png")
    thumbnailTwo = models.ImageField(null=True, blank=True, upload_to="img", default="placeholder.png")
    thumbnailThree = models.ImageField(null=True, blank=True, upload_to="img", default="placeholder.png")
    liveLink = models.URLField(null=True, blank=True)
    codeLink = models.URLField(null=True, blank=True)
    body = RichTextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, null=True)
    slug = models.SlugField(null=True, blank=True) 

    def __str__(self):
        return self.headline


    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.headline)

            has_slug = Post.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.headline) + '-' + str(count) 
                has_slug = Post.objects.filter(slug=slug).exists()

            self.slug = slug

        super().save(*args, **kwargs)
