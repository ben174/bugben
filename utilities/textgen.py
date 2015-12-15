import textwrap
from django.utils.html import strip_tags

class TextResumeGenerator:
    """
    Takes a Resume from bugben's Resume model
    and turns it into a nicely-formatted text blob,
    with configurable column width.

    Author: Ben Friedland (ben@bugben.com)

    """

    def __init__(self, resume):
        self.resume = resume

    def to_text(self, text_width=80):
        resume = self.resume
        header = ' Resume Of '.center(text_width, '-')
        ret = header + '\n'
        ret += resume.name.upper().center(text_width) + '\n'
        ret += resume.email.center(text_width) + '\n'
        ret += resume.url.center(text_width) + '\n'
        ret += '-' * text_width + '\n'
        ret += '\n\n'

        # profile summary
        ret += 'PROFILE SUMMARY'.ljust(text_width, '.') + '\n'
        ret += '\n'
        for entry in resume.profileentry_set.all():
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
        for link in resume.importantlink_set.all():
            ret += ' * ' + link.description + ': ' + link.url + '\n'
        ret += '\n\n'

        # expertise
        ret += 'EXPERTISE'.ljust(text_width, '.') + '\n'
        ret += '\n'
        for entry in resume.expertiseentry_set.all():
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
        for entry in resume.workhistoryentry_set.all():
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
        for project in resume.project_set.all():
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
