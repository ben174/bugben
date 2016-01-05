from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView
from resume.models import Resume
from rikeripsum import rikeripsum
from utilities.textgen import TextResumeGenerator


class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'resume/resume_detail.html'

    def get(self, request, format=None, *args, **kwargs):
        resume = Resume.objects.first()

        # If someone curls my resume, return plain text
        if request.META.get('HTTP_USER_AGENT', '').startswith('curl'):
            format = 'text'

        if format == 'text' or format == 'plain':
            gen = TextResumeGenerator(resume)
            text_width = int(request.GET.get('columns', '80'))
            ret = gen.to_text(text_width=80)
            return HttpResponse(ret, content_type='text/plain')

        return render(request, self.template_name, {
            'object': resume,
            'format': format,
        })


def riker(self):
    ret = rikeripsum.generate_paragraph()
    return HttpResponse(ret, content_type='text/plain')

