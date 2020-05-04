import requests
import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.http import HttpResponse

from .models import Tool, Category, Activity, Tag, Level, Inspiration, Page, Resource

# Create your views here.
def index(request):
    activities = Activity.objects.filter(is_published=True)
    levels = Level.objects.all()
    banner = Page.objects.filter(slug="welcome-banner").first()
    return render(request, "tools/activities.html", 
            {'activities': activities,
            'levels':levels, 
            'banner':banner
            } )

def view(request, slug):
    activity = Activity.objects.filter(slug=slug).first()

    return render(request, "tools/activity.html", {'activity': activity} )

def page(request, slug):
    page = Page.objects.filter(slug=slug).first()
    return render(request, "tools/page.html", {'page': page,} )

def tag(request, tag):
    tag = Tag.objects.filter(slug=tag).first()

    tools = Tool.objects.filter(tags=tag).order_by('?')
    inspirations = Inspiration.objects.filter(tags=tag).order_by('?')
    resources = Resource.objects.filter(tags=tag).order_by('?')

    return render(request, "tools/tag.html", {'tag': tag, 'tools':tools, 'inspirations':inspirations,'resources':resources} )


def tags(request):
    banner = Page.objects.filter(slug="tags").first()
    tags = Tag.objects.all()

    return render(request, "tools/tags.html", {'tags': tags,  'banner':banner} )

def tools(request):
    tools = Tool.objects.all().order_by('?')
    banner = Page.objects.filter(slug="tools").first()
    return render(request, "tools/tools.html", {'tools': tools,  'banner':banner} )

def inspirations(request):
    banner = Page.objects.filter(slug="inspirations").first()
    inspirations = Inspiration.objects.all().order_by('?')

    return render(request, "tools/inspirations.html", {'inspirations': inspirations,  'banner':banner} )

def resources(request):
    banner = Page.objects.filter(slug="resources").first()
    resources = Resource.objects.all().order_by('?')

    return render(request, "tools/resources.html", {'resources': resources,  'banner':banner} )


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
    inspirations =[]
    if query:
        tools = Tool.objects.filter( Q(name__contains=query)|Q(about__contains=query) )
        tags = Tag.objects.filter(slug__contains=tag).first()
        inspirations = Inspiration.objects.filter(Q(name__contains=query)|Q(about__contains=query) )
        activities = Activity.objects.filter(Q(name__contains=query)|Q(preamble__contains=query))

    results = results   + list(activities) + list(tools) +list(inspirations)

    return render(request, "tools/searchresults.html", {'results': results,'query':query} )



