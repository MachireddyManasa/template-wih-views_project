from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *

def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)


def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    return render(request,'display_webpage.html',context=d)


def display_records(request):
    LOA=AccessRecords.objects.all()
    d={'accessrecords':LOA}
    return render(request,'display_records.html',context=d)


