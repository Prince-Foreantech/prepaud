from django.db import models
from autoslug import AutoSlugField
# from ckeditor.fields import RichTextField
from djrichtextfield.models import RichTextField
class blog_details(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='blog/images')
    category = models.CharField(max_length=1000)
    tags = models.TextField()
    content = RichTextField()
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)

    def __str__(self):
        return self.title

    