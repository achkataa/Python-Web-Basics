from Expenses_Tracker.main.models import Profile
from django import template

register = template.Library()


@register.simple_tag()
def has_profile():
    return Profile.objects.count() > 0