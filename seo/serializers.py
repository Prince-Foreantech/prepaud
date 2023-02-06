from rest_framework import serializers
from .models import *


class seo_category_sr(serializers.Serializer):
    class Meta:
        model = seo_category
        fields = ('category')


class seo_discription_sr(serializers.ModelSerializer):
    
    category = seo_category_sr(required=True)
    class Meta:
        model = seo_discription
        fields = ('category','title','url','slug')