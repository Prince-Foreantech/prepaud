from django.db import models
from autoslug import AutoSlugField
class audiolist(models.Model):
    title = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='audio/feature_images')
    audio = models.FileField(upload_to='audio/audiofile')
    
    discription = models.TextField()
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    date_time = models.DateTimeField()

    def __str__(self):
        return self.title
