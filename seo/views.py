from django.shortcuts import render
from .models import seo_discription, seo_category


def discription(request):

    get_dis = seo_category.objects.all()
    return render(request,"abc.html",{"data":get_dis})
