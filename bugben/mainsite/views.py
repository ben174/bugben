from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils.html import strip_tags
from mainsite.models import *

import textwrap

def home(request, output_format=None):
    data = resume_dict()
    data['format'] = output_format
    if output_format == 'plain': 
        text_width = 80
        if request.GET.get('c', ''): 
            try: 
                text_width = int(request.GET.get('c', ''))
            except: 
                pass
        return HttpResponse(generate_text_resume(text_width), 
                content_type='text/plain')
    else: 
        return render(request, 'mainsite/home.html', data)


def generate_text_resume(text_width): 
    data = resume_dict()

    header = ' Resume Of '.center(text_width, '-')
    ret = header + '\n'
    ret += data['resume'].name.upper().center(text_width) + '\n'
    ret += data['resume'].email.center(text_width) + '\n'
    ret += data['resume'].url.center(text_width) + '\n'
    ret += '-' * text_width + '\n'
    ret += '\n\n'

    # profile summary
    ret += 'PROFILE SUMMARY'.ljust(text_width, '.') + '\n'
    ret += '\n'
    for entry in data['profile_entries']:
        wrapped = textwrap.fill(entry.entry, text_width-3, 
                subsequent_indent='   ') 
        ret += ' * ' + wrapped + '\n'
    ret += '\n\n'

    # links
    ret += 'LINKS'.ljust(text_width, '.') + '\n'
    ret += '\n'
    for link in data['important_links']:
        ret += ' * ' + link.description + ': ' + link.url + '\n'
    ret += '\n\n'

    # expertise
    ret += 'EXPERTISE'.ljust(text_width, '.') + '\n'
    ret += '\n'
    for entry in data['expertise_entries']:
        ret += '   ' + entry.entry.upper() + '\n'
        wrapped = textwrap.fill(entry.entry_details, text_width-3, 
                subsequent_indent='   ') 
        ret += '   ' + wrapped + '\n'
        ret += '\n'
    ret += '\n\n'

    # experience
    ret += 'EXPERIENCE'.ljust(text_width, '.') + '\n'
    ret += '\n'
    for entry in data['work_history_entries']:
        ret += '   ' + entry.client_name.upper() + '\n'
        ret += '   ' + entry.location + '\n'
        ret += '   ' + entry.timespan + '\n'
        ret += '   ' + entry.title + '\n'
        ret += '\n'
        for achievement in entry.workachievement_set.all(): 
            wrapped = textwrap.fill(achievement.description, text_width-6, 
                subsequent_indent='      ') 
            ret += '      ' + wrapped + '\n'
            ret += '\n'
        ret += '\n\n'

    # contributions
    ret += 'COMMUNITY CONTRIBUTIONS'.ljust(text_width, '.') + '\n'
    ret += '\n'
    for project in data['projects']:
        ret += '   ' + project.name.upper() + '\n'
        wrapped = textwrap.fill(strip_tags(project.short_description), 
            text_width-3, subsequent_indent='   ') 
        ret += '   ' + wrapped + '\n'
        wrapped = textwrap.fill(strip_tags(project.long_description),
            text_width-3, subsequent_indent='   ') 
        ret += '   ' + wrapped + '\n\n'
        if project.deployment_url: 
            ret += '      Project Page: %s\n' % project.deployment_url
            ret += '      Source Code:  %s\n' % project.src_url
        ret += '\n\n'
    

    tag_line_top = "The code to generate this resume was written by me."
    tag_line_bottom = "See the code at http://github.com/ben174/bugben"
    
    ret += '-' * text_width + '\n'
    ret += tag_line_top.center(text_width) + '\n'
    ret += tag_line_bottom.center(text_width) + '\n'
    ret += '-' * text_width + '\n'
    return ret

    



def resume_dict(): 
    resume = Resume.objects.all()[0]
    projects = Project.objects.all()
    profile_entries = ProfileEntry.objects.all()
    important_links = ImportantLink.objects.all()
    expertise_entries = ExpertiseEntry.objects.all()
    work_history_entries = WorkHistoryEntry.objects.all()
    return { 
        'resume': resume,
        'projects': projects, 
        'profile_entries': profile_entries,
        'important_links': important_links,
        'expertise_entries': expertise_entries,
        'work_history_entries': work_history_entries,
    }
