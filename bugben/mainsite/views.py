from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from mainsite.models import *

def home(request):
    return render(request, 'mainsite/home.html', { })

