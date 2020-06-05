from django import template
from django.utils.safestring import mark_safe


register = template.Library()


def text_to_html(value):
    """Turns plain text into HTML"""
    return mark_safe(value.replace('\n', '<br>'))


register.filter('text_to_html', text_to_html)
