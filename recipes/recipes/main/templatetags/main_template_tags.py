from django import template
register = template.Library()

@register.filter()
def separate_by_comma(string):
    return string.split(', ')