try:
    import requests
except:
    print ("Can't import requests")
import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.http import HttpResponse
from django.http import JsonResponse

from .models import *

# Create your views here.
def index(request):
    status = request.GET.get('before_we_begin')
    print("before_we_begin",status)
    if status == None: 
        levels = Level.objects.filter(order__gte = 0).filter(order__lt = 4)
        activities = Activity.objects.filter(is_published=True).filter(level__order__gt=-1).filter(level__order__lt=4).order_by('level__order')
    else: # BEFORE WE BEGIN!
        levels = Level.objects.filter(order__lt = 0)
        activities = Activity.objects.filter(level__order__lt=0).order_by('level__order')

    
    banner = Page.objects.filter(slug="welcome-banner").first()
    return render(request, "tools/activities.html", 
            {'activities': activities,
            'levels':levels, 
            'banner':banner
            } )

def view(request, slug):
    activity = Activity.objects.filter(slug=slug).first()
    #gather learnings up

    has_learnings = False
    learnings = list(activity.learnings.all())
   

    for tool in activity.tools.all():
        tool_learnings = tool.learnings.all()
        for learning in tool_learnings:
            if learning in learnings:
                pass
            else:
                learnings.append(learning)

    if len(learnings) > 0:
         has_learnings = True

    return render(request, "tools/activity.html",
         {'activity': activity,
        'learnings': learnings,
        'has_learnings':has_learnings} )


def team(request):
    people = Person.objects.all()
    return render(request, "tools/team.html", {'people': people,} )

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
    levels = Level.objects.filter(order__gte = 0).filter(order__lt = 5)
    return render(request, "tools/tools.html", {'tools': tools,  'banner':banner, 'levels':levels} )

def latest(request):
    tools = Tool.objects.all().order_by('-id')[0:25]
    inspirations = Inspiration.objects.all().order_by('-id')[0:25]
    resources = Resource.objects.all().order_by('-id')[0:15]

    banner = Page.objects.filter(slug="latest").first()
    levels = Level.objects.filter(order__gte = 0).filter(order__lt = 25)

    results = list(tools)+list(inspirations)+list(resources)
    
    return render(request, "tools/latest.html", {'tools': results,  'banner':banner, 'levels':levels} )

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
    resources = []

    if query:
        tools = Tool.objects.filter( Q(name__contains=query)|Q(about__contains=query) )
        tags = Tag.objects.filter(slug__contains=tag).first()
        inspirations = Inspiration.objects.filter(Q(name__contains=query)|Q(about__contains=query) )
        resources = Resource.objects.filter(Q(name__contains=query)|Q(about__contains=query) )
        activities = Activity.objects.filter(Q(name__contains=query)|Q(preamble__contains=query))

    results = results   + list(activities) + list(tools) +list(inspirations) + list(resources)

    return render(request, "tools/searchresults.html", {'results': results,'query':query} )

def slotmachine(request):
    # See: https://codepen.io/AdrianSandu/pen/MyBQYz
    #query = request.GET.get("q", False)
    results = []
    tools = []
    tags =[]
    activities = []
    inspirations =[]
    

    #tags = Tag.objects.all().order_by('?')[0:20]
    tools = Tool.objects.all().order_by('?')
    tcount = int(tools.count())
    inspirations = Inspiration.objects.all().order_by('?')
    icount = int(inspirations.count())
    resources = Resource.objects.all().order_by('?')
    rcount = int(resources.count())

    smallest = min( tcount, icount, rcount)
    print("smallest", smallest)
    tools = tools[0:smallest]
    inspirations = inspirations[0:smallest]
    resources = resources[0:smallest]

    #activity = Activity.objects.all().order_by('?').first()


    return render(request, "tools/slotmachine.html", {
    'tools':tools, 'inspirations':inspirations, 'resources':resources} )

def api(request):
    #query = request.GET.get("q", False)
    results = []
    tools = []
    tags =[]
    activities = []
    inspirations =[]
    
    tools = Tool.objects.all().order_by('?').all().values('name', 'url', 'image_url', 'about','category__name','altcategory__name')
    inspirations = Inspiration.objects.all().order_by('?').all().values('name', 'url', 'image_url', 'about','category__name','altcategory__name')
    resources = Resource.objects.all().order_by('?').all().values('name', 'url', 'image_url', 'about','category__name','altcategory__name')
    
    results = list( list(tools) + list(inspirations) + list(resources))
    return JsonResponse(results, safe=False)
    
    #return render(request, "tools/api.html", {'results':results, 'inspirations':inspirations, 'resources':resources} )



