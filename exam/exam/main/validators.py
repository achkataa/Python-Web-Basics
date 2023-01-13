from django.core.exceptions import ValidationError
import re


def only_letters_validator(value):
    if not re.match(r'^[A-Za-z0-9_]+$', value):
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore.')