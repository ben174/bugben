from django.shortcuts import render
from django.views.generic import DetailView
from resume.models import Resume


def home(request):
    return ResumeDetailView.as_view()(request, Resume.objects.first())


class ResumeDetailView(DetailView):
    model = Resume
