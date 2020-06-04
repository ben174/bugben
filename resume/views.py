from django.shortcuts import render
from resume.models import Resume


def resume(request):
    return render(request, 'resume.html', {'resume': Resume.objects.first()})
