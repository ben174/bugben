from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils.html import strip_tags
from mainsite.models import *

import textwrap
import docx
import tempfile


def home(request, output_format=None):
    data = resume_dict()
    data['format'] = output_format
    if output_format == 'plain':
        text_width = 80
        if request.GET.get('columns', ''):
            try:
                text_width = int(request.GET.get('columns', ''))
            except:
                pass
        return HttpResponse(
            generate_text_resume(text_width),
            content_type='text/plain'
        )
    elif output_format == 'doc':
        docx_mime_type = 'application/vnd.openxmlformats-officedocument.' \
                'wordprocessingml.document'
        return HttpResponse(
            generate_docx_resume(),
            content_type=docx_mime_type,
        )
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
        wrapped = textwrap.fill(
            entry.entry,
            text_width-3,
            subsequent_indent='   '
        )
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
        wrapped = textwrap.fill(
            entry.entry_details,
            text_width-3,
            subsequent_indent='   ',
        )
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
            wrapped = textwrap.fill(
                achievement.description,
                text_width-6,
                subsequent_indent='      ',
            )
            ret += '      ' + wrapped + '\n'
            ret += '\n'
        ret += '\n\n'

    # contributions
    ret += 'COMMUNITY CONTRIBUTIONS'.ljust(text_width, '.') + '\n'
    ret += '\n'
    for project in data['projects']:
        ret += '   ' + project.name.upper() + '\n'
        wrapped = textwrap.fill(
            strip_tags(project.short_description),
            text_width-3,
            subsequent_indent='   ',
        )
        ret += '   ' + wrapped + '\n'
        wrapped = textwrap.fill(
            strip_tags(project.long_description),
            text_width-3,
            subsequent_indent='   ',
        )
        ret += '   ' + wrapped + '\n\n'
        if project.deployment_url:
            ret += '      Project Page: %s\n' % project.deployment_url
            ret += '      Source Code:  %s\n' % project.src_url
        ret += '\n\n'

    tag_line_top = "This is my plain text resume generator"
    tag_line_middle = "Outputting at %s columns" % text_width
    tag_line_bottom = "http://github.com/ben174/bugben"

    ret += '-' * text_width + '\n'
    ret += tag_line_top.center(text_width) + '\n'
    ret += tag_line_middle.center(text_width) + '\n'
    ret += tag_line_bottom.center(text_width) + '\n'
    ret += '-' * text_width + '\n'
    return ret


def generate_docx_resume():
    relationships = docx.relationshiplist()
    document = docx.newdocument()
    body = document.xpath('/w:document/w:body', namespaces=docx.nsprefixes)[0]
    data = resume_dict()

    body.append(docx.heading('Resume of', 3))
    body.append(docx.heading(data['resume'].name, 1))
    body.append(docx.heading(data['resume'].email, 2))
    body.append(docx.heading(data['resume'].url, 2))

    body.append(docx.heading('PROFILE SUMMARY', 2))
    for entry in data['profile_entries']:
        body.append(docx.paragraph(entry.entry, style='ListBullet'))

    body.append(docx.heading('LINKS', 2))
    for link in data['important_links']:
        body.append(docx.paragraph('%s - %s' % (
            link.description,
            link.url,
        ), style='ListBullet'))

    body.append(docx.heading('EXPERTISE', 2))
    for entry in data['expertise_entries']:
        body.append(docx.paragraph(entry.entry, style='ListBullet'))


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
            wrapped = textwrap.fill(
                achievement.description,
                text_width-6,
                subsequent_indent='      ',
            )
            ret += '      ' + wrapped + '\n'
            ret += '\n'
        ret += '\n\n'

    # contributions
    ret += 'COMMUNITY CONTRIBUTIONS'.ljust(text_width, '.') + '\n'
    ret += '\n'
    for project in data['projects']:
        ret += '   ' + project.name.upper() + '\n'
        wrapped = textwrap.fill(
            strip_tags(project.short_description),
            text_width-3,
            subsequent_indent='   ',
        )
        ret += '   ' + wrapped + '\n'
        wrapped = textwrap.fill(
            strip_tags(project.long_description),
            text_width-3,
            subsequent_indent='   ',
        )
        ret += '   ' + wrapped + '\n\n'
        if project.deployment_url:
            ret += '      Project Page: %s\n' % project.deployment_url
            ret += '      Source Code:  %s\n' % project.src_url
        ret += '\n\n'

    tag_line_top = "This is my plain text resume generator"
    tag_line_middle = "Outputting at %s columns" % text_width
    tag_line_bottom = "http://github.com/ben174/bugben"

    ret += '-' * text_width + '\n'
    ret += tag_line_top.center(text_width) + '\n'
    ret += tag_line_middle.center(text_width) + '\n'
    ret += tag_line_bottom.center(text_width) + '\n'
    ret += '-' * text_width + '\n'



    # Create our properties, contenttypes, and other support files
    title    = 'Resume of %s' % data['resume'].name
    subject  = 'My awesome resume!'
    creator  =  data['resume'].name
    keywords = []

    coreprops = docx.coreproperties(
        title=title,
        subject=subject,
        creator=creator,
        keywords=keywords,
    )
    appprops = docx.appproperties()
    contenttypes = docx.contenttypes()
    websettings = docx.websettings()
    wordrelationships = docx.wordrelationships(relationships)


    data = None
    with tempfile.NamedTemporaryFile() as temp:
        docx.savedocx(
            document,
            coreprops,
            appprops,
            contenttypes,
            websettings,
            wordrelationships,
            temp.name
        )
        data = open(temp.name).read()
    return data


def resume_dict():
    resume = Resume.objects.all()[0]
    projects = Project.objects.all().order_by('sort_order')
    profile_entries = ProfileEntry.objects.all().order_by('sort_order')
    important_links = ImportantLink.objects.all().order_by('sort_order')
    expertise_entries = ExpertiseEntry.objects.all().order_by('sort_order')
    work_hist_entries = WorkHistoryEntry.objects.all().order_by('sort_order')
    return {
        'resume': resume,
        'projects': projects,
        'profile_entries': profile_entries,
        'important_links': important_links,
        'expertise_entries': expertise_entries,
        'work_history_entries': work_hist_entries,
    }
