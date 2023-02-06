from rest_framework import serializers

class audiolist_sr(serializers.Serializer):
    title = serializers.CharField(max_length=500)
    thumbnail = serializers.ImageField()
    discription = serializers.CharField(max_length=500)
    audio = serializers.FileField()
    slug = serializers.SlugField()
    date = serializers.DateTimeField()