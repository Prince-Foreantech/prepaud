from django.shortcuts import render
from django.http import HttpResponse
from .models import audiolist
from rest_framework.renderers import JSONRenderer
from .serializers import audiolist_sr
def audio(request):
    if request.method == 'GET':
        a = audiolist.objects.all()
        b = audiolist_sr(a,many=True)
        data = JSONRenderer().render(b.data)
        return HttpResponse(data,content_type='application/json')

