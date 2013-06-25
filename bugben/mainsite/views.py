from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from mainsite.models import *

def home(request):
    resume = Resume.objects.all()[0]
    projects = Project.objects.all()
    profile_entries = ProfileEntry.objects.all()
    important_links = ImportantLink.objects.all()
    expertise_entries = ExpertiseEntry.objects.all()
    return render(request, 'mainsite/home.html', { 
        'resume': resume,
        'projects': projects, 
        'profile_entries': profile_entries,
        'important_links': important_links,
        'expertise_entries': expertise_entries,
    })

