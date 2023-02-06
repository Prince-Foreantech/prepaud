from rest_framework import serializers
class blog_details_sr(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    image = serializers.ImageField()
    content = serializers.CharField(max_length=1000)
    category = serializers.CharField(max_length=1000)
    tags = serializers.CharField()
    slug = serializers.SlugField()