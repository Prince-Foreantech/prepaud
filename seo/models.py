from django.db import models
from autoslug import AutoSlugField
# Create your models here.
class seo_category(models.Model):
    category = models.CharField(max_length=500)

    def __str__(self):
        return self.category

class seo_discription(models.Model):
    category = models.ForeignKey(seo_category, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)

    def __str__(self):
        return self.title