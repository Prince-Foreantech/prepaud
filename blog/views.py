from django.http import HttpResponse
from .models import blog_details
from .serializers import blog_details_sr
from rest_framework.renderers import JSONRenderer
def blog(request):
    if request.method == "GET":
        all_blog = blog_details.objects.all()
        all_blog_sr = blog_details_sr(all_blog, many=True)
        data = JSONRenderer().render(all_blog_sr.data)
        return HttpResponse(data, content_type="application/json")

