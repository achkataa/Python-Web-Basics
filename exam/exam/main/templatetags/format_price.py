from django import template
register = template.Library()

@register.filter()
def format_to_the_second_decimal_place(price):
    return f'{price:.2f}'