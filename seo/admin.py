from django.contrib import admin

# Register your models here.

from .models import seo_category, seo_discription

admin.site.register(seo_category)
admin.site.register(seo_discription)