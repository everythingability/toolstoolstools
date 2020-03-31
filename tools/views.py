import requests
import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.http import HttpResponse

from .models import Tool, Category, Activity, Tag

# Create your views here.
def index(request):
    activities = Activity.objects.filter(is_published=True)

    return render(request, "tools/activities.html", 
            {'activities': activities,

            } )

def view(request, slug):
    activity = Activity.objects.filter(slug=slug).first()

    return render(request, "tools/activity.html", {'activity': activity} )

def tag(request, tag):
    tag = Tag.objects.filter(slug=tag).first()

    tools = Tool.objects.filter(tags=tag)

    return render(request, "tools/tag.html", {'tag': tag, 'tools':tools} )

def tools(request):
    tools = Tool.objects.all()

    return render(request, "tools/tools.html", {'tools': tools} )

from django.contrib.auth import logout
from django.http import JsonResponse

def do_logout(request):
    logout(request)

    return redirect("/")

def search(request):
    query = request.GET.get("q", False)
    results = []
    tools = []
    tags =[]
    activities = []
    if query:
        tools = Tool.objects.filter(Q(name__contains=query)|Q(about__contains=query))
        tags = Tag.objects.filter(slug__contains=tag).first()
        activities = Activity.objects.filter(Q(name__contains=query)|Q(preamble__contains=query))

    results = results + list(tools)  + list(activities)

    return render(request, "tools/searchresults.html", {'results': results,} )



